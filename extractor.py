API_KEY = '07ff973ae3c65130f89b72cb033902ec'
API_SECRET = 'RLlhwFY8j-iE4vk30-AadNqWYTsKz2-h'

import time
from pprint import pformat
from facepp import API
api = API(API_KEY, API_SECRET)

# import requests
def print_result(hint, result):
    def encode(obj):
        if type(obj) is unicode:
            return obj.encode('utf-8')
        if type(obj) is dict:
            return {encode(k): encode(v) for (k, v) in obj.iteritems()}
        if type(obj) is list:
            return [encode(i) for i in obj]
        return obj
    # print hint
    result = encode(result)
    return '\n'.join(['  ' + i for i in pformat(result, width = 75).split('\n')])


IMAGE_DIR = 'http://cn.faceplusplus.com/static/resources/python_demo/'

MALE_PERSONS_TRAINING = ['abdurezak.jpg', 'darius.jpg', 'jerry.jpg', 'louis.jpg', 'pavan.jpg', 'alan.jpg', 'davey.jpg', 'jimmie.jpg', 'louisa.jpg', 'pepe.jpg', 'alec.jpg', 'david.jpg', 'jin.jpg', 'luran.jpg', 'peyten.jpg', 'alex.jpg', 'deven.jpg', 'joe.jpg', 'mack.jpg', 'pradeep.jpg', 'andy.jpg', 'donovan.jpg', 'john.jpg', 'mandela.jpg', 'priten.jpp', 'andyw.jpg', 'dylan.jpg', 'johnny.jpg', 'marcus.jpg', 'sam.jpg', 'austin.jpg', 'eduardo.jpg', 'jon.jpg', 'marlon.jpg', 'samuel.jpg', 'basel.jpg', 'erez.jpg', 'jonathan.jpg', 'matt.jpg', 'samuell.jpg', 'ben.jpg', 'erik.jpg', 'jordan.jpg', 'mattj.jpg', 'sunui.jpg', 'bruno.jpg', 'filip.jpg', 'josh.jpg', 'max.jpg', 'tim.jpg', 'bryan.jpg', 'grant.jpg', 'joshua.jpg', 'maxh.jpg', 'timothy.jpg', 'caleb.jpg', 'handong.jpg', 'jovin.jpg', 'mezu.jpg', 'timothy1.jpg', 'cesar.jpg', 'henry.jpg', 'jullia.jpg', 'michael.jpg', 'tristen.jpg', 'chris.jpg', 'ilde.jpg', 'justin.jpg', 'michaela.jpg', 'tyler.jpg', 'christian.jpg', 'jackson.jpg', 'justus.jpg', 'michaels.jpg', 'tylerf.jpg', 'cole.jpg', 'jake.jpg', 'kamran.jpg', 'mirza.jpg', 'valentino.jpg', 'conor.jpg', 'jamie.jpg', 'kevin.jpg', 'nathan.jpg', 'william.jpg', 'daniel.jpg', 'jason.jpg', 'kevins.jpg', 'neel.jpg', 'williaml.jpg', 'danielr.jpg', 'jasonc.jpg', 'kevon.jpg', 'omar.jpg', 'willie.jpg', 'daren.jpg', 'jean.jpg', 'leszek.jpg', 'pablo.jpg', 'wyatt.jpg']
FEMALE_PERSONS_TRAINING = []
MALE_PERSONS_TEST = []
FEMALE_PERSONS_TEST = []

PERSONS = []
def split_list(alist, wanted_parts=1):
    length = len(alist)
    return [alist[i*length // wanted_parts: (i+1)*length // wanted_parts] for i in range(wanted_parts)]

for name in MALE_PERSONS_TRAINING:
    PERSONS.append((name,"http://web.stanford.edu/~kirbygee/tinder/male/" + name))

TARGET_IMAGE = IMAGE_DIR + '4.jpg'

smallpeople = split_list(PERSONS, 5)
smallpeople = []

MALE_PERSONS_TRAINING_1 = ['abdurezak.jpg', 'darius.jpg', 'jerry.jpg', 'louis.jpg', 'pavan.jpg', 'alan.jpg', 'davey.jpg', 'jimmie.jpg', 'louisa.jpg', 'pepe.jpg']
MALE_PERSONS_TRAINING_2 = ['alec.jpg', 'david.jpg', 'jin.jpg', 'luran.jpg', 'peyten.jpg', 'alex.jpg', 'deven.jpg', 'joe.jpg', 'mack.jpg', 'pradeep.jpg']
MALE_PERSONS_TRAINING_3 = ['andy.jpg', 'donovan.jpg', 'john.jpg', 'mandela.jpg', 'priten.jpp', 'andyw.jpg', 'dylan.jpg', 'johnny.jpg', 'marcus.jpg', 'sam.jpg']
MALE_PERSONS_TRAINING_4 = ['austin.jpg', 'eduardo.jpg', 'jon.jpg', 'marlon.jpg', 'samuel.jpg', 'basel.jpg', 'erez.jpg', 'jonathan.jpg', 'matt.jpg', 'samuell.jpg']
MALE_PERSONS_TRAINING_5 = ['ben.jpg', 'erik.jpg', 'jordan.jpg', 'mattj.jpg', 'sunui.jpg', 'bruno.jpg', 'filip.jpg', 'josh.jpg', 'max.jpg', 'tim.jpg']
MALE_PERSONS_TRAINING_6 = ['bryan.jpg', 'grant.jpg', 'joshua.jpg', 'maxh.jpg', 'timothy.jpg', 'caleb.jpg', 'handong.jpg', 'jovin.jpg', 'mezu.jpg', 'timothy1.jpg']
MALE_PERSONS_TRAINING_7 = ['cesar.jpg', 'henry.jpg', 'jullia.jpg', 'michael.jpg', 'tristen.jpg', 'chris.jpg', 'ilde.jpg', 'justin.jpg', 'michaela.jpg', 'tyler.jpg']
MALE_PERSONS_TRAINING_8 = ['christian.jpg', 'jackson.jpg', 'justus.jpg', 'michaels.jpg', 'tylerf.jpg', 'cole.jpg', 'jake.jpg', 'kamran.jpg', 'mirza.jpg', 'valentino.jpg']
MALE_PERSONS_TRAINING_9 = ['conor.jpg', 'jamie.jpg', 'kevin.jpg', 'nathan.jpg', 'william.jpg', 'daniel.jpg', 'jason.jpg', 'kevins.jpg', 'neel.jpg', 'williaml.jpg']
MALE_PERSONS_TRAINING_10 = ['danielr.jpg', 'jasonc.jpg', 'kevon.jpg', 'omar.jpg', 'willie.jpg', 'daren.jpg', 'jean.jpg', 'leszek.jpg', 'pablo.jpg', 'wyatt.jpg']

FEMALE_PERSONS_TRAINING_1 = ['aakrati.jpg', 'adrianna.jpg', 'aisha.jpg', 'alice.jpg', 'allie.jpg', 'alliej.jpg', 'amanda.jpg', 'amandaf.jpg', 'amy.jpg', 'ana.jpg'] 
FEMALE_PERSONS_TRAINING_2 = ['andrea.jpg', 'angelina.jpg', 'anna.jpg', 'annak.jpg', 'annie.jpg', 'aran.jpg', 'arianna.jpg', 'ariannac.jpg', 'august.jpg', 'belle.jpg']
FEMALE_PERSONS_TRAINING_3 = ['birdie.jpg', 'brittany.jpg', 'brynn.jpg', 'caitlin.jpg', 'camille.jpg', 'camillen.jpg', 'chelsea.jpg', 'christine.jpg', 'claudia.jpg', 'courtney.jpg']
FEMALE_PERSONS_TRAINING_4 = ['cristina.jpg', 'cynthia.jpg', 'daniela.jpg', 'eda.jpg', 'eehjoon.jpg', 'eleasha.jpg', 'elena.jpg', 'elenia.jpg', 'ellen.jpg', 'embree.jpg']
FEMALE_PERSONS_TRAINING_5 = ['emi.jpg', 'emily.jpg', 'emilyt.jpg', 'emilyw.jpg', 'emilyz.jpg', 'esther.jpg', 'fiona.jpg', 'francesca.jpg', 'gerda.jpg', 'grazie.jpg']
FEMALE_PERSONS_TRAINING_6 = ['hanel.jpg', 'hannah.jpg', 'hayley.jpg', 'hellary.jpg', 'isabel.jpg', 'izzi.jpg', 'jeewon.jpg', 'jessie.jpg', 'julia.jpg', 'kahanui.jpg']
FEMALE_PERSONS_TRAINING_7 = ['kaitlin.jpg', 'katherine.jpg', 'katherinep.jpg', 'kim.jpg', 'kyliez.jpg', 'laura.jpg', 'leila.jpg', 'maria.jpg', 'marissa.jpg', 'melody.jpg']
FEMALE_PERSONS_TRAINING_8 = ['michaela.jpg', 'michelle.jpg', 'minnie.jpg', 'nagham.jpg', 'natasha.jpg', 'neha.jpg', 'nora.jpg', 'noura.jpg', 'phoebe.jpg', 'priyanka.jpg']
FEMALE_PERSONS_TRAINING_9 = ['sara.jpg', 'sarafina.jpg', 'sarah.jpg', 'sarahf.jpg', 'sarahj.jpg', 'schyler.jpg', 'sharon.jpg', 'shingshing.jpg', 'siri.jpg', 'sofia.jpg']
FEMALE_PERSONS_TRAINING_10 = ['sofiag.jpg', 'solange.jpg', 'stephanie.jpg', 'varsha.jpg', 'vera.jpg', 'waverley.jpg', 'yehong.jpg', 'ying.jpg', 'zayan.jpg', 'zizi.jpg']

smallpeople = [MALE_PERSONS_TRAINING_1, MALE_PERSONS_TRAINING_2, MALE_PERSONS_TRAINING_3, MALE_PERSONS_TRAINING_4, MALE_PERSONS_TRAINING_5, MALE_PERSONS_TRAINING_6, MALE_PERSONS_TRAINING_7, MALE_PERSONS_TRAINING_8, MALE_PERSONS_TRAINING_9, MALE_PERSONS_TRAINING_10]

# idx = 1
# for arr in smallpeople:
#     print 'Making Api Call %d / %d' % (idx, len(smallpeople))
#     FACES = {name: api.detection.detect(url = url) for name, url in arr}
#     for name, face in FACES.iteritems():
#         print_result(name, face)
#     time.sleep(120)
#     idx += 1

arr = []
# for name in MALE_PERSONS_TRAINING_1:
#     arr.append((name,"http://web.stanford.edu/~kirbygee/tinder/male/" + name))


for name in FEMALE_PERSONS_TRAINING_4:
    arr.append((name,"http://web.stanford.edu/~kirbygee/tinder/female/" + name))

FACES = {name: api.detection.detect(url = url) for name, url in arr}
# for name, face in FACES.iteritems():
#     face_dict = face
#     face_dict = face_dict['face'][0]
#     for k, v in face_dict.iteritems():
#         print k, v

for name, face in FACES.iteritems():
    print print_result(name, face)

# smallpeople = split_list(PERSONS)
# for arr in smallpeople:
#     FACES = {name: api.detection.detect(url = url)
#         for name, url in arr}
    
#     for name, face in FACES.iteritems():
#         print_result(name, face)