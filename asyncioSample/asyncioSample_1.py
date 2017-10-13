import asyncio
import datetime
from urllib.request import Request, urlopen
import requests
from bs4 import BeautifulSoup
#python 3.4
# @asyncio.coroutine
# def functionName():
#     yield from ~

#python 3.5 over
# async def functionName():
#     await ~~

# async def sample():
#     print('hello python  world')
#
# loop = asyncio.get_event_loop()
# loop.run_until_complete(sample())
# loop.close()

# async def add(a, b):
#     print('add function start')
#     await asyncio.sleep(3)
#     return a + b
#
# async def add_result(a, b):
#     startTime = datetime.datetime.now()
#     print('startTime :: ', startTime)
#     result = await add(a, b)
#     endTime = datetime.datetime.now()
#     print('endtime :: ', endTime)
#     #print(endTime - startTime)
#     print('result :: {0} + {1} =  {2}'.format(a, b, result))
#
# loop = asyncio.get_event_loop()
# loop.run_until_complete(add_result(5, 7))
# loop.close()

#---------------------------2start------------------------------------------
#비동기 처리
#https://search.yahoo.com/search?p=naver
keyword = ['python', 'c#', 'java', 'c', 'javascript']
urls = ['https://search.yahoo.com/search?p=' + i for i in keyword]
print(urls)
async def fetch(url):
    try:
        response = await loop.run_in_executor(None, requests.get, url)
        return response
        # soup = BeautifulSoup(response.content, 'html.parser')
        # for keyword in soup.find_all(class_=' ac-1st fc-5th fz-ms'):
        #     print(keyword.text)
    except:
        import traceback
        print(traceback.format_exc())

async def main():
    tasks = [asyncio.ensure_future(fetch(url)) for url in urls]
    result = await asyncio.gather(*tasks)
    print(result)

startTimeV1 = datetime.datetime.now()
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()
endTimeV1 = datetime.datetime.now()
duraionV1 = endTimeV1 - startTimeV1
print(duraionV1)

#일반
startTimeV2 = datetime.datetime.now()
responseList = []
for url in urls:
    response = requests.get(url)
    responseList.append(response)
print(responseList)
endTimeV2 = datetime.datetime.now()
print(endTimeV2-startTimeV1)
#---------------------------2end------------------------------------------



