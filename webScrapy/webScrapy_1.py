from urllib.request import urlopen, HTTPError
from bs4 import BeautifulSoup
import traceback

# try:
#     html = urlopen('website...')
#
# except HTTPError as e:
#     print(e)
#     print(traceback.format_exc())
# else:
#     bsObj = BeautifulSoup(html.read(), 'html.parser')
#
#     if bsObj.h1 is not None:
#         print(bsObj.h1)
#     if bsObj.html.h2 is not None:
#         print(bsObj.html.h2)


def getTag(url, tagName='h1'):
    try:
        html = urlopen(url)
    except HTTPError as error:
        print(error.msg)
        return None

    try:
        bsObj = BeautifulSoup(html.read(), 'html.parser')
        if tagName == 'h1':
            tagText = bsObj.html.h1

    except AttributeError as e:
        return None
    return tagText



#tagText = getTag('websites...')
#if tagText is None:
#    print(' %s not found ', tagText)"h1",
#else:
#    print(tagText)


html = urlopen('')
bsObj = BeautifulSoup(html, 'html.parser')
spanTagData = bsObj.findAll("span", {"class": "green"})
#for tagData in spanTagData:
    #print(tagData) #tag with print
    #print(tagData.get_text()) #tag ignore print

hTag = bsObj.findAll({"h1", "h2", "h3", "h4", "h5", "h6"})
for tag in hTag:
    print(tag)




