import redis
import traceback
import ast

#redis connection
r = redis.StrictRedis(host='localhost', port=6379, db=0, charset='utf-8', decode_responses=True)

def redisSet(key, value):
    if r.get(key) is None:
        result = r.set(key, value)

        return result

def redisGet(key):
    result = r.get(key)
    return result


try:
    #redis data insert
    cityData = {"countryCode": "JP", "nameEn": "japan", "nameKo": "일본"}

    citycode = "JPTYOKO"
    key = "cityCode:"+citycode

    result = redisSet(key, cityData)

    if result:
        resultStrData = redisGet(key)
        resultDict = ast.literal_eval(resultStrData)

        print(resultDict['nameEn'])

except:
    print(traceback)

