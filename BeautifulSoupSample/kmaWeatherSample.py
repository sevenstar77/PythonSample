import requests
import traceback
from bs4 import BeautifulSoup
import asyncio
from datetime import datetime


def connection(url, method, params=None, data=None, timeout=100):
    if method.lower() == 'get':
        if params is not None:
            response = requests.get(url, params=params)
            result = responseCheck(response)
            if result:
                response = response.text

        else:
            response = requests.get(url)

            result = responseCheck(response)
            if result:
                response = response.content

    if method.lower() == 'post':
        pass
    return response


def responseCheck(response):
    if response.status_code == 200:
        return True
    else:
        raise ConnectionError

def icornData_get(rs):
    soupRs = BeautifulSoup(rs, "lxml")
    #tbody = soupRs.find('tbody')
    #print(tbody)
    # bodyData = tbody.select('img')

    bodyDatas = soupRs.select('tbody img')
    dataDict = {}

    for bodyData in bodyDatas:
        key, value = _get_wehaterIcorn(bodyData)
        if key:
            dataDict[key] = value

    return dataDict

def _get_wehaterIcorn(data):

    name = data.get('alt')
    fileName = data.get('src')

    if name not in ('강수 아이콘 구분 안내', '부이'):
        return fileName.split('/')[-1].split('.')[0], name
    return False, None

if __name__ == "__main__":

    #TODO 기상청 아이콘 이미지별 날씨정보
    icornData = {}
    icornUlrs = 'http://www.kma.go.kr/weather/icon_info.html'
    rs = connection(icornUlrs, method='get')
    icornData = icornData_get(rs)
    print('icornData : ', icornData)

    #서울 구 별 현재 날씨 정보
    #구별 코드
    #강남구 : 1168000000 /