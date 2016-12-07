API_KEY = '07ff973ae3c65130f89b72cb033902ec'
API_SECRET = 'RLlhwFY8j-iE4vk30-AadNqWYTsKz2-h'

import time
from pprint import pformat
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
    print hint
    result = encode(result)
    print '\n'.join(['  ' + i for i in pformat(result, width = 75).split('\n')])

from facepp import API
api = API(API_KEY, API_SECRET)

IMAGE_DIR = 'http://cn.faceplusplus.com/static/resources/python_demo/'
# r = requests.post('http://httpbin.org/post', files={'report.xls': open('report.xls', 'rb')})
PERSONS = [
    # ('Jim Parsons', IMAGE_DIR + '1.jpg'),
    # ('Leonardo DiCaprio', IMAGE_DIR + '2.jpg'),
    # ('Andy Liu', IMAGE_DIR + '3.jpg'),
    # ('Tina Zheng', 'https://s13.postimg.org/5eal9h24n/tina.jpg'),
    # ('Sharyn Lee','https://s15.postimg.org/agxnnu7rv/sharyn1.jpg'),
    ('Meghana Rao', 'https://s17.postimg.org/63gf1u2yn/meghana.jpg'),
    # ('Kirby Gee', 'https://s14.postimg.org/4fivpnolt/kirby2.jpg')
    # ('Brexton Pham', 'https://s14.postimg.org/4btng7jb5/brexton2.png'),
    # ('Meghana Rao', 'https://s21.postimg.org/gq83ye5gn/meghana_4.jpg')
    # ('Ngoc Bui', 'https://s13.postimg.org/htfvrqrbr/ngoc.jpg'),
    # ('Ben Josie', 'https://s15.postimg.org/gfyj663vf/ben_josie.jpg')
    # ('Darby Schumacher', 'https://s11.postimg.org/seesrvwpv/darby.jpg')
    # ('Dan Yu', 'https://s13.postimg.org/hr1njizev/dan.jpg')
    # ('Jina Yoo', 'https://s17.postimg.org/gj007whjz/jina.jpg')
    # ('Daren', 'http://web.stanford.edu/~kirbygee/tinder/male/davey.jpg')
    # http://i1.kym-cdn.com/entries/icons/original/000/019/712/48029_ori.jpg

]
TARGET_IMAGE = IMAGE_DIR + '4.jpg'

FACES = {name: api.detection.detect(url = url)
        for name, url in PERSONS}

for name, face in FACES.iteritems():
    print_result(name, face)