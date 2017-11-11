import json
"""
data -> json파일이 저장 serialization
json파일 -> data deserialization


function
--직렬화
1. dump() 텍스트 파일에 파이썬 객체를 내보낸다.
2. dumps() 파이썬 객체를 텍스트 문자열로 내보낸다.

--역직렬화
3. load() json 문자열을 파이썬 객체로 가져온다.
4. loads() 2개이상의 문자열 데이터를 리스트 형식의 파이썬 객체로 가져온다.
"""

path = "txtSample/sample1.json"

json_data = {
  "name": "monkey",
  "age": "55",
  "address": "jungle"
}

# with open(path, "w") as export_json:
#     json.dump(json_data, export_json, indent=None, sort_keys=False)
#

with open(path) as import_json:
    obj1 = json.load(import_json)
    print(type(obj1))

print(obj1)
json_string = json.dumps(obj1)

obj2 = json.loads((json_string))
print(obj2)





