import requests
from bs4 import BeautifulSoup
import asyncio
import traceback
try:
    url = 'https://search.yahoo.com/search?p=python'
    response = requests.get(url)

    soup = BeautifulSoup(response.content, 'html.parser')
    #print(soup)

    for keyword in soup.find_all(class_=' ac-1st fc-5th fz-ms'):
        print(keyword.text)

except:
    traceback.format_exc()
