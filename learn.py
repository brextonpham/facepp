# convert json file into matrix
# import pandas

import json
import csv

from pprint import pprint

with open('male.json') as data_file:
    data = json.load(data_file)

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

table = []
usedNames = set()
for row in data['males']:
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
            table.append(newPerson)
        usedNames.add(name)
    else:
        print 'no face for ' + row['url']


ratings = []
i = 0
with open('femaleRatings.csv', 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
        if i > 0:
            ratings.append(row)
        i += 1

for person in table:
    name = person[NAME]
    for rating in ratings:
        if rating[0].replace(".jpg", "") == name:
            person['Megs'] = rating[1]
            person['Helen'] = rating[2]
            person['Sharon'] = rating[3]


df = pandas.DataFrame(table)
df = df.sort_values(by=NAME, ascending=1)
print df
males = df.as_matrix()
print(males)
