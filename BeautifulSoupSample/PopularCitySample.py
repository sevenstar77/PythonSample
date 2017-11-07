from bs4 import BeautifulSoup
import traceback
import requests

#TODO 여행사이트의 인기도시주요 목록 데이터 가져오기

def gateWayClient(urls,  method='get', params=None, data=None ):
    rs = ''
    if method.lower() == 'get':
        response = requests.get(urls, params)
        if response.status_code == 200:
            rs = response.text
    if method.lower() == 'post':
        pass
    return rs

def get_popularCity(rs):
    try:
        results = []
        resultDict = {}

        soup = BeautifulSoup(rs, "lxml")
        search_contents = soup.select('div.quick_search_body > div.tab_contents')

        for search_content in search_contents:
            #print(search_content)
            contents = search_content.select('div.quick_city > a')
            popularCountry = contents[0].text
            cityLists = []
            for city in search_content.select('div.quick_city > a')[1:]:
                cityLists.append(city.text)
            resultDict[popularCountry] = cityLists
        results.append(resultDict)

        return results
    except:
        print(traceback.format_exc())

if __name__ == "__main__":
    #path = input()
    # domain = '***'
    # urls = domain + '/' + path

    urls = input()

    rs = gateWayClient(urls)
    results = get_popularCity(rs)

    print(results)




