# convert json file into matrix
import pandas
import csv
import json
from sklearn import linear_model
from sklearn import neighbors
from sklearn import ensemble
from sklearn import svm
from sklearn import tree

from sklearn import preprocessing

from pprint import pprint

gender = 'female'

with open(gender + '.json') as data_file:
    data = json.load(data_file)


with open('test_' + gender + '.json') as data_file:
    testData = json.load(data_file)

pprint(data)

AGE = 'age'
GENDER = 'gender'
RACE = 'race'
SMILING = 'smiling'
# x and y coordinates
CENTER = 'center'
EYE_LEFT = 'eye_left'
EYE_RIGHT = 'eye_right'
MOUTH_LEFT = 'mouth_left'
MOUTH_RIGHT = 'mouth_right'
NOSE = 'nose'

HEIGHT = 'height'
WIDTH = 'width'

NAME = 'name'
HOT = 'hot'

# read train data
trainTable = []
usedNames = set()
for row in data[gender]:
    face = row['face']
    newPerson = {}
    if len(face) > 0:
        # get all attributes
        attr = face[0]['attribute']
        newPerson[AGE] = str(attr[AGE]['value'])
        newPerson[RACE] = str(attr[RACE]['value'])
        newPerson[SMILING] = str(attr[SMILING]['value'])

        # get all position
        pos = face[0]['position']
        newPerson[CENTER + '_X'] = str(pos[CENTER]['x'])
        newPerson[CENTER + '_Y'] = str(pos[CENTER]['y'])
        newPerson[EYE_LEFT + '_X'] = str(pos[EYE_LEFT]['x'])
        newPerson[EYE_LEFT + '_Y'] = str(pos[EYE_LEFT]['y'])
        newPerson[EYE_RIGHT + '_X'] = str(pos[EYE_RIGHT]['x'])
        newPerson[EYE_RIGHT + '_Y'] = str(pos[EYE_RIGHT]['y'])
        newPerson[MOUTH_LEFT + '_X'] = str(pos[MOUTH_LEFT]['x'])
        newPerson[MOUTH_LEFT + '_Y'] = str(pos[MOUTH_LEFT]['y'])
        newPerson[MOUTH_RIGHT + '_X'] = str(pos[MOUTH_RIGHT]['x'])
        newPerson[MOUTH_RIGHT + '_Y'] = str(pos[MOUTH_RIGHT]['y'])
        newPerson[NOSE + '_X'] = str(pos[NOSE]['x'])
        newPerson[NOSE + '_Y'] = str(pos[NOSE]['y'])

        newPerson[HEIGHT] = str(pos[HEIGHT])
        newPerson[WIDTH] = str(pos[WIDTH])

        name = str(row['url'][row['url'].rfind('/') + 1 : -4])
        newPerson[NAME] = name
        if name not in usedNames:
            trainTable.append(newPerson)
        usedNames.add(name)
    else:
        print 'no face for ' + row['url']


ratings = []
i = 0
with open(gender + 'Ratings.csv', 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
        if i > 0:
            ratings.append(row)
        i += 1

for person in trainTable:
    name = person[NAME]

    for rating in ratings:
        if rating[0].replace(".jpg", "") == name:
            if gender == 'male':
                person['Megs'] = str(rating[1])
                person['Helen'] = str(rating[2])
                person['Sharon'] = str(rating[3])
            else:
                person['Zach'] = str(rating[1])
                person['Brexton'] = str(rating[2])
                person['Kirby'] = str(rating[3])


df = pandas.DataFrame(trainTable)
df = df.sort_values(by=NAME, ascending=1)
df = df.drop('name', 1)
# read test data
testTable = []
usedNames = set()
for row in testData[gender]:
    face = row['face']
    newPerson = {}
    if len(face) > 0:
        # get all attributes
        attr = face[0]['attribute']
        newPerson[AGE] = str(attr[AGE]['value'])
        newPerson[RACE] = str(attr[RACE]['value'])
        newPerson[SMILING] = str(attr[SMILING]['value'])

        # get all position
        pos = face[0]['position']
        newPerson[CENTER + '_X'] = str(pos[CENTER]['x'])
        newPerson[CENTER + '_Y'] = str(pos[CENTER]['y'])
        newPerson[EYE_LEFT + '_X'] = str(pos[EYE_LEFT]['x'])
        newPerson[EYE_LEFT + '_Y'] = str(pos[EYE_LEFT]['y'])
        newPerson[EYE_RIGHT + '_X'] = str(pos[EYE_RIGHT]['x'])
        newPerson[EYE_RIGHT + '_Y'] = str(pos[EYE_RIGHT]['y'])
        newPerson[MOUTH_LEFT + '_X'] = str(pos[MOUTH_LEFT]['x'])
        newPerson[MOUTH_LEFT + '_Y'] = str(pos[MOUTH_LEFT]['y'])
        newPerson[MOUTH_RIGHT + '_X'] = str(pos[MOUTH_RIGHT]['x'])
        newPerson[MOUTH_RIGHT + '_Y'] = str(pos[MOUTH_RIGHT]['y'])
        newPerson[NOSE + '_X'] = str(pos[NOSE]['x'])
        newPerson[NOSE + '_Y'] = str(pos[NOSE]['y'])

        newPerson[HEIGHT] = str(pos[HEIGHT])
        newPerson[WIDTH] = str(pos[WIDTH])

        name = str(row['url'][row['url'].rfind('/') + 1 : -4])
        newPerson[NAME] = name
        if name not in usedNames:
            testTable.append(newPerson)
        usedNames.add(name)
    else:
        print 'no face for ' + row['url']

ratings = []
i = 0
with open('test' + gender + 'Ratings.csv', 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
        if i > 0:
            ratings.append(row)
        i += 1
for person in testTable:
    name = person[NAME]

    for rating in ratings:
        if rating[0].replace(".jpg", "") == name:
            if gender == 'male':
                person['Megs'] = str(rating[1])
                person['Helen'] = str(rating[2])
                person['Sharon'] = str(rating[3])
            else:
                person['Zach'] = str(rating[1])
                person['Brexton'] = str(rating[2])
                person['Kirby'] = str(rating[3])

dfTest = pandas.DataFrame(testTable)
dfTest = dfTest.sort_values(by=NAME, ascending=1)
dfTest = dfTest.drop('name', 1)

if gender == 'male':
    trainHelen = df.drop('Megs', 1).drop('Sharon', 1)
    trainMegs = df.drop('Helen', 1).drop('Sharon', 1)
    trainSharon = df.drop('Megs', 1).drop('Helen', 1)

    le = preprocessing.LabelEncoder()
    le.fit(trainSharon.race)
    trainSharon.race = [str(r) for r in le.transform(trainSharon.race)]

    trainSharon = trainSharon.as_matrix()

    #toggle the binary classifier
    # reg = linear_model.LogisticRegression()
    reg = ensemble.GradientBoostingClassifier()
    # reg = neighbors.KNeighborsClassifier()
    reg.fit(trainSharon[:,1:], trainSharon[:,0])
    # print reg.coef_

    likes = 0
    predictedLikes = 0
    correctPredictions = 0
    for i, p in enumerate(reg.predict(trainSharon[:,1:])):
        actual = trainSharon[:,0][i]
        if actual == '1':
            likes += 1
        if p == '1':
            predictedLikes += 1
        if p == '1' and actual == '1':
            correctPredictions += 1

    print likes, predictedLikes, correctPredictions
    print 'actual likes: ', likes
    print 'predicted likes: ', predictedLikes
    print 'precision: ', float(correctPredictions) / predictedLikes
    print 'recall: ', float(correctPredictions) / likes
else:
    trainZach = df.drop('Brexton', 1).drop('Kirby', 1)
    testZach = dfTest.drop('Brexton', 1).drop('Kirby', 1)

    trainKirby = df.drop('Zach', 1).drop('Brexton', 1)
    testKirby = dfTest.drop('Zach', 1).drop('Brexton', 1)

    trainBrexton = df.drop('Zach', 1).drop('Kirby', 1)
    testBrexton = dfTest.drop('Zach', 1).drop('Kirby', 1)

    # reg = linear_model.LogisticRegression()
    # reg = ensemble.GradientBoostingClassifier()
    # reg = neighbors.KNeighborsClassifier()
    # reg = ensemble.RandomForestClassifier()
    # reg = tree.DecisionTreeClassifier()
    # reg = linear_model.RidgeClassifier()

    # reg = linear_model.PassiveAggressiveClassifier()
    # reg = svm.SVC()

    classifiers = [
                (linear_model.LogisticRegression(), 'LogisticRegression'),
                (ensemble.GradientBoostingClassifier(), 'GradientBoostingClassifier'),
                (neighbors.KNeighborsClassifier(), 'KNeighborsClassifier'),
                (ensemble.RandomForestClassifier(), 'RandomForestClassifier'),
                (tree.DecisionTreeClassifier(), 'DecisionTreeClassifier'),
                (linear_model.RidgeClassifier(), 'RidgeClassifier')
            ]

    trials = [(trainZach, testZach, 'Zach'), (trainKirby, testKirby, 'Kirby'), (trainBrexton, testBrexton, 'Brexton')]

    for trial in trials:
        trainSet, testSet, name = trial
        le = preprocessing.LabelEncoder()
        le.fit(trainBrexton.race)
        trainSet.race = [str(r) for r in le.transform(trainSet.race)]
        testSet.race = [str(r) for r in le.transform(testSet.race)]

        trainSet = trainSet.as_matrix()
        testSet = testSet.as_matrix()

        print '++++++++ %s ++++++++' % (trial[2])
        for classifier in classifiers:
            reg, classifierName = classifier


            reg.fit(trainSet[:,1:], trainSet[:,0])

            likes = 0
            predictedLikes = 0
            correctPredictions = 0

            for i, p in enumerate(reg.predict(testSet[:,1:])):
                actual = testSet[:,0][i]
                if actual == '1':
                    likes += 1
                if p == '1':
                    predictedLikes += 1
                if p == '1' and actual == '1':
                    correctPredictions += 1

            print 'classifier: ' + classifierName
            # print likes, predictedLikes, correctPredictions
            print 'actual likes: ', likes
            print 'predicted likes: ', predictedLikes
            print 'precision: ', float(correctPredictions) / predictedLikes
            print 'recall: ', float(correctPredictions) / likes
            print '\n'
        print '\n'
