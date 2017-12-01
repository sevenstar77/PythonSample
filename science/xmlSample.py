from bs4 import BeautifulSoup
import requests
import os

url = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108"
savename = "forecast.xml"

if not os.path.exists(savename):
    res = requests.get(url)

    with open(savename, "wb") as f:
        f.write(res.content)

xml = open(savename, "r", encoding="utf-8").read()
soup = BeautifulSoup(xml, 'html.parser')

info = {}
for location in soup.find_all("location"):
    name = location.find('city').string
    wheather = location.find('wf').string
    if not (wheather in info):
        info[wheather] = []
    info[wheather].append(name)

#print(info)
for wheather in info.keys():
    print(wheather)
    for city in info[wheather]:
        print(city)