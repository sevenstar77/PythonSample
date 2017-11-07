from bs4 import BeautifulSoup
import traceback
import requests
import lxml

def connection(url, method, params=None, data=None, timeout=100):
    if method.lower() == 'get':
        if params is not None:
            response = requests.get(url, params=params)
            result = responseCheck(response)
            if result:
                response = response.content

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

def naver_keywrod(responseData):
    results = []
    soup = BeautifulSoup(responseData, 'lxml')
    keywordRs = soup.select('div.ah_roll_area.PM_CL_realtimeKeyword_rolling > ul > li')

    for keyword in keywordRs:
        result = {}
        keywordNo = keyword.find('span', {'class': 'ah_r'}).text
        keywordName = keyword.find('span', {'class': 'ah_k'}).text
        result[keywordNo] = keywordName
        results.append(result)
    return results


if __name__ == '__main__':
    urls = 'http://www.naver.com'
    rs = connection(urls, 'get')

    result = naver_keywrod(rs)
    print(result)

