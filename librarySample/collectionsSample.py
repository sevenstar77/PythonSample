import collections
c = collections.Counter()
c['test'] +=1
c['ak'] += 1
c['ak'] += 10
c['ak'] += 100
#print(c)

counts = collections.Counter(
    [1,2,3,1,2,3,3,2,7]
)

#print(counts)
#print(counts[8])

counter1 = collections.Counter(red=5, black=3, blue=2, yellow=3)
counter2 = collections.Counter(red=2, yellow=5)

result1 = counter1 + counter2
print('+ : ', result1)

result2 = counter1 - counter2
print(' - : ', result2)

result3 = counter1 & counter2
print(' & : ', result3)

result4 = counter1 | counter2
print(' | : ', result4)

def defaultValue():
    return 0

import traceback
try:
    dataDict_1 = {'red' : 5, 'black': 4}
    dataDict_2 = {'blue': 2, 'yellow': 3}
    print(type(dataDict_1))
    print(type(dataDict_2))
    dataDict = collections.ChainMap(dataDict_1, dataDict_2)
    print(dataDict)
    print(dataDict['red'])
    dataDict['puple'] = 6
    print(dataDict)

    default = collections.defaultdict(defaultValue, green=4)
    print('default', default)
    print(default['pink'])
except:
    print('error~')
    print(traceback.format_exc())



names = {'kim' : 1, 'jin' : 2, 'park': 3, 'jo': 4, 'lee': 5, 'ho': 6}

# for name in names:
#     print(name)

import json

datas = collections.OrderedDict(names)

#print(datas)
#print(datas['jin'])
for key, data in datas.items():
    print('key : {0}, value : {1}'.format(key, data))

jsonDatas = json.dumps(datas)
print('type : ', type(jsonDatas))
print('json : ', jsonDatas)
