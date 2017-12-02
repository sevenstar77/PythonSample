import requests
import os.path, random
import json


url = "http://validate.jsontest.com/?json=[JSON-code-to-validate]"

savename = 'sampleJson1.json'

if not os.path.exists(url):
    with open(savename, 'wb') as b:
        res = requests.get(url)
        print(type(res.content))
        b.write(res.content)



items = json.load(open(savename, 'r', encoding="utf-8"))
#print(type(items))
#print(type(json.dumps(items)))
print(items)
print(items['object_or_array'])

#for item in items:
#    print(item["object_or_array"] + "====" + item['validate'])