from dateutil.parser import parse
from datetime import datetime

result1 = parse('2018/01/01 00:00:01')
print(result1)
result2 = parse('2018/01/01')
print(result2)
result3 = parse('2018-07-07')
print(result3)
result4 = parse('20180505')
print(result4)
result5 = parse('Tue, 23 Nov 2017 11:11:00 GMT')
print(result5)

