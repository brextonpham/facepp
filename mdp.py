import collections
from collections import defaultdict 
import random
from copy import deepcopy
from math import floor
import math


class QLearning():
    def __init__(self, actions, discount, featureExtractor, explorationProb=0.2):
        self.actions = actions
        self.discount = discount
        self.featureExtractor = featureExtractor
        self.explorationProb = explorationProb
        self.weights = defaultdict(float)
        self.numIters = 0

    def Q(self, state, action):
        return sum([self.weights[feature] * val for feature, val in self.featureExtractor(state, action)])

    def getAction(self, state):
        self.numIters += 1
        if random.random() < self.explorationProb:
            return random.choice(self.actions(state))
        else:
            return max([(self.Q(state, action), action) for action in self.actions(state)])[1]

    def getStepSize(self):
        return 1 / math.sqrt(self.numIters)

    def incorporateFeedback(self, state, action, reward, newState):
        self.numIters += 1
        if newState == None:
            Vopt_sprime = 0
        else:
            Vopt_sprime = max([self.Q(newState, newAction) for newAction in self.actions(newState)])

        prediction = self.Q(state, action)
        target = reward + self.discount * Vopt_sprime
        adjustment = self.getStepSize() * (target - prediction)

        features = self.featureExtractor(state, action)
        for f, v in features:
            self.weights[f] = self.weights[f] + adjustment * v

class ValueIteration():
   
    def solve(self, mdp, epsilon=0.001):
        mdp.computeStates()
        def computeQ(mdp, V, state, action):
            # Return Q(state, action) based on V(state).
            return sum(prob * (reward + mdp.discount() * V[newState]) \
                            for newState, prob, reward in mdp.succAndProbReward(state, action))

        def computeOptimalPolicy(mdp, V):
            # Return the optimal policy given the values V.
            pi = {}
            for state in mdp.states:
                pi[state] = max((computeQ(mdp, V, state, action), action) for action in mdp.actions(state))[1]
            return pi

        V = collections.defaultdict(float)  # state -> value of state
        numIters = 0
        maxIters = 10000
        while True and numIters < maxIters:
            newV = {}
            for state in mdp.states:
                newV[state] = max(computeQ(mdp, V, state, action) for action in mdp.actions(state))
            numIters += 1
            if (float(numIters) / maxIters) == 0.25: print '25% Done'
            if (float(numIters) / maxIters) == 0.50: print '50% Done'
            if (float(numIters) / maxIters) == 0.75: print '75% Done'
            change = max(abs(V[state] - newV[state]) for state in mdp.states)
            if change < epsilon:
                V = newV
                break
            V = newV

        # Compute the optimal policy now
        pi = computeOptimalPolicy(mdp, V)
        print "ValueIteration: %d iterations" % numIters
        self.pi = pi
        self.V = V



class tinderMDP():
    def __init__(self, likingScores, numPeople):
        self.likingScores = likingScores
        self.numPeople = numPeople
        self.likeBackProb = 0.15

    def startState(self):
        return (random.randint(0, numPeople - 1), 50)

    def actions(self, state):
        return ["swipe right", "swipe left"]

    def succAndProbReward(self, state, action):
        person, swipesRemaining = state
        if person == None or swipesRemaining == 0: return []
        if action == "swipe right":
            results = []
            results.append(((None, None), self.likeBackProb, self.likingScores[person]))
            for p in range(self.numPeople):
                results.append(((p, swipesRemaining - 1), (1 - self.likeBackProb) / self.numPeople, 0))
            return results
        else:
            #action is swipe left
            results = []
            for p in range(self.numPeople):
                results.append(((p, swipesRemaining - 1), float(1) / self.numPeople, 0))
            return results

    def computeStates(self):
        self.states = set()
        self.states.add((None, None))
        for swipesRemaining in range(51):
            for p in range(self.numPeople):
                self.states.add((p, swipesRemaining))
    def discount(self):
        return 1



def simulate(mdp, ql=None, pi=None, numTrials=1000, maxIterations=10000, verbose=False,
             sort=False):
    # Return i in [0, ..., len(probs)-1] with probability probs[i].
    def sample(probs):
        target = random.random()
        accum = 0
        for i, prob in enumerate(probs):
            accum += prob
            if accum >= target: return i
        raise Exception("Invalid probs: %s" % probs)

    totalRewards = []  # The rewards we get on each trial
    for trial in range(numTrials):
        state = mdp.startState()
        sequence = [state]
        totalDiscount = 1
        totalReward = 0
        for _ in range(maxIterations):
            if pi:
                action = pi[state]
            else:
                action = ql.getAction(state)

            transitions = mdp.succAndProbReward(state, action)
            if sort: transitions = sorted(transitions)
            if len(transitions) == 0:
                if not pi:
                    ql.incorporateFeedback(state, action, 0, None)
                break

            # Choose a random transition
            i = sample([prob for newState, prob, reward in transitions])
            newState, prob, reward = transitions[i]
            sequence.append(action)
            sequence.append(reward)
            sequence.append(newState)

            if not pi:
                ql.incorporateFeedback(state, action, reward, newState)
            totalReward += totalDiscount * reward
            totalDiscount *= mdp.discount()
            state = newState
        if verbose:
            print "Trial %d (totalReward = %s): %s" % (trial, totalReward, sequence)
        totalRewards.append(totalReward)
    return totalRewards

numPeople = 10
likingScores = range(1, 11)
def featureExtractor(state, action):
    person, swipesRemaining = state
    if person == None or swipesRemaining == 0: return []
    return [((likingScores[person], action), 1), ((swipesRemaining, action), 1), ((likingScores[person], swipesRemaining, action), 1)]



# mdp = tinderMDP(likingScores, numPeople)
# ql = QLearning(mdp.actions, mdp.discount(), featureExtractor)
# print 'Performing QLearning...'
# simulate(mdp, ql, numTrials=500000)
# ql.explorationProb = 0
# totalRewards = simulate(mdp, ql, numTrials=500000)
# #print 'Total Rewards: ', totalRewards
# print 'Total Rewards Average (QLearning): ', float(sum(totalRewards)) / len(totalRewards)
# #print ql.weights

# ql.explorationProb = 1
# print 'Simulating Random Policy...'
# totalRewardsRandom = simulate(mdp, ql, numTrials=500000)
# #print 'Total Rewards (Random): ', totalRewardsRandom
# print 'Average (Random): ', float(sum(totalRewardsRandom)) / len(totalRewardsRandom)

mdp = tinderMDP(likingScores, numPeople)
VI = ValueIteration()
print 'Performing Value Iteration...'
VI.solve(mdp)
totalRewardsVI = simulate(mdp, pi=VI.pi, numTrials=10000)
print 'Average (VI): ', float(sum(totalRewardsVI)) / len(totalRewardsVI)
showValueIterationPolicy = True
if showValueIterationPolicy:
    for state, action in sorted(VI.pi.iteritems(), key = lambda t: (t[0][0], t[0][1])):
        person, swipesRemaining = state
        if person != None:
            print (likingScores[person], swipesRemaining), action




