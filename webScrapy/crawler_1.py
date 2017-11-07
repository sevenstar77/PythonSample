import traceback
import re
import requests
from bs4 import BeautifulSoup
from urllib.error import HTTPError


def download(url, method='GET', headers=None, retryCount=3):
    html = ''
    try:
        if headers is None:
            headers = {'User-agent': 'wswp'}

        if method.upper() == 'GET':
            html = requests.get(url=url, headers=headers).content
            if isinstance(html, bytes):
                html = html.decode('utf-8')

    except HTTPError as e:
        html = None

        if retryCount > 0:
            if hasattr(e, 'code') and 500 <= e.code < 600:
                return download(url, retryCount=-1)
    except:
        html = None
        print(traceback.format_exc())
    return html


def crawler_siteMap(url):
    try:
        siteMapResponse = download(url)
        print(siteMapResponse)
        links = re.findall('<loc>(.*?)</loc>', siteMapResponse)
        #links = re.findall('<header>(.*?)</header>', siteMapResponse)
        print(links)
        for link in links:
            html = download(link)
            print(html)
    except:
        print(traceback.format_exc())


crawler_siteMap('sample url')

