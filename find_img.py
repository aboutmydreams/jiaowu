import requests,time
import base64
import numpy as np
from PIL import Image
from io import BytesIO
from collections import Counter

def get_token():
    host =  'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=ir3vbkVgKHywSDrzLASDpFAT&client_secret=ctvu2kbwBSX3C5kGiXC66F1fRp1VcoiI'
    headers = {
        'Content-Type':'application/json;charset=UTF-8'
    }
    res = requests.get(url=host,headers=headers).json()
    return res['access_token']

def baidu(base64img):
    data = {}
    # data['access_taken'] = res['access_token']
    data['access_taken'] = '24.3d4e3aad2b1fa147d57c934e4efc0122.2592000.1549177627.282335-11416205'
    url = 'https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic' + 'user/add?access_token=' + data['access_taken']
    data['image'] = base64img
    headers={
        "Content-Type":"application/x-www-form-urlencoded",
    }
    res = requests.post(url=url,headers=headers,data=data)
    result = res.json()
    wod = result["words_result"]
    # for i in wod:
    #     print(i['words'])
    return str(wod[0]['words'])


def imgs(allsave = 0,cookie1=None):
    url = 'http://jwc104.ncu.edu.cn:8081/jsxsd/verifycode.servlet'
    bd_session = requests.Session()
    if not cookie1:
        response = bd_session.get(url)
        cookii = requests.utils.dict_from_cookiejar(response.cookies)
        # print(cookii)
    else:
        cookii = cookie1
        headers = {
            'Cookie': cookie1,
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36',
        }
        response = bd_session.get(url, headers=headers)
    img = Image.open(BytesIO(response.content))

    if allsave == 1:
        t = time.time()
        file_name = str(int(round(t * 1000)))
        img.save('imgs/{}.png'.format(file_name))
        file = open('imgs/{}.png'.format(file_name),'rb')
        image = file.read()
        img_base64 = base64.b64encode(image)
        file.close()
    else:
        img.save('imgs/1.png')
        file = open('imgs/1.png','rb')
        image = file.read()
        img_base64 = base64.b64encode(image)
        file.close()
    return img_base64


def all_np(arr):
    t1 = time.time()
    arr = np.array(arr)
    key = np.unique(arr)
    result = {}
    for k in key:
        mask = (arr == k)
        arr_new = arr[mask]
        v = arr_new.size
        result[k] = v
    t2 = time.time()
    print (t2-t1)
    return result



def get_count_by_counter(l):
    t1 = time.time()
    count = Counter(l)
    t2 = time.time()
    print (t2-t1)
    count_dict = dict(count)
    return count_dict

n = 0
answers = []
while n < 1000:
    try:
        imgbase = imgs(1)
        num = baidu(imgbase)
        answers.append(num)
        n += 1
    except BaseException as e:
        print(e)
        pass 


print(answers)

file0 = open('data.txt','a+')
file0.write(str(answers))
file0.close()

cout1 = get_count_by_counter(answers)
file1 = open('cont1.txt','w')
file1.write(str(cout1))
file1.close()

cout2 = all_np(answers)
file2 = open('cont2.txt','w')
file2.write(str(cout2))
file2.close()