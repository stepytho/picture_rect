import requests
import base64
import json
import time

from urllib.request import urlopen
from urllib.request import Request
from urllib.error import URLError
from urllib.parse import urlencode
from urllib.parse import quote_plus
        
APP_ID = '23981884'
API_KEY = 'grtlt8VeYbY01lrmoZqRNOZC'
SECRET_KEY = '8Wl1kPmxYfURvOOYHkDum0MiHV37XBtf'
TOKEN_URL = 'https://aip.baidubce.com/oauth/2.0/token'

#已删除截图部分代码
def fetch_token():
    params = {'grant_type': 'client_credentials',
              'client_id': API_KEY,
              'client_secret': SECRET_KEY}
    post_data = urlencode(params)
    
    post_data = post_data.encode('utf-8')
    req = Request(TOKEN_URL, post_data)
    try:
        f = urlopen(req, timeout=5)
        result_str = f.read()
    except URLError as err:
        print(err)
    
    result_str = result_str.decode()
    result = json.loads(result_str)

    if ('access_token' in result.keys() and 'scope' in result.keys()):
        if not 'brain_all_scope' in result['scope'].split(' '):
            print ('please ensure has check the  ability')
            exit()
        return result['access_token']
    else:
        print ('please overwrite the correct API_KEY and SECRET_KEY')
        exit()

'''
数字识别
'''
def main():
    request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/numbers"
    # 二进制方式打开图片文件
    f = open('test.png', 'rb')
    img = base64.b64encode(f.read())

    params = {"image":img}
    access_token = fetch_token()
    request_url = request_url + "?access_token=" + access_token
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    response = requests.post(request_url, data=params, headers=headers)

    numbers = []
    if response:
        #print (response.json())
        for i in response.json()["words_result"]:
            numbers.append(i["words"])

    #print(numbers)
    #for i in range(len(numbers)):
       # print("第%d个数是%s" %(i+1, numbers[i]))

    return numbers

def main_angle():
    #screen()
    request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/numbers"
    # 二进制方式打开图片文件
    f = open('test_angle.png', 'rb')
    img = base64.b64encode(f.read())

    params = {"image":img}
    access_token = fetch_token()
    request_url = request_url + "?access_token=" + access_token
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    response = requests.post(request_url, data=params, headers=headers)

    numbers = []
    if response:
        #print (response.json())
        for i in response.json()["words_result"]:
            numbers.append(i["words"])

    #print(numbers)
    #for i in range(len(numbers)):
       # print("第%d个数是%s" %(i+1, numbers[i]))

    return numbers

if __name__ == "__main__":
    main()