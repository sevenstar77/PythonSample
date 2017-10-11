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

async def add(a, b):
    print('add function start')
    await asyncio.sleep(3)
    return a + b

async def add_result(a, b):
    startTime = datetime.datetime.now()
    print('startTime :: ', startTime)
    result = await add(a, b)
    endTime = datetime.datetime.now()
    print('endtime :: ', endTime)
    #print(endTime - startTime)
    print('result :: {0} + {1} =  {2}'.format(a, b, result))

loop = asyncio.get_event_loop()
loop.run_until_complete(add_result(5, 7))
loop.close()


#https://search.yahoo.com/search?p=naver
keyword = ['python', 'c#', 'java', 'c', 'javascript']
urls = ['https://search.yahoo.com/search?p=' + i for i in keyword]

# async def fetch(url):
#     #response = requests.get(url)
#     loop = asyncio.get_event_loop()
#     response = await loop.run_in_executor(None, requests.get, url)
#
#     soup = BeautifulSoup(response.content, 'html.parser')
#
#     for keyword in soup.find_all(class_=' ac-1st fc-5th fz-ms'):
#         print(keyword.text)
#
# async def main():
#     tasks = [asyncio.ensure_future(fetch(url)) for url in urls]


