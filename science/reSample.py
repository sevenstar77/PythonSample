import re
result1 = re.split(r'\W', "hello, reSample!~")
print(result1)


result2 = re.split(r'\W+', "hello, reSample!~")
print(result2)


#match(pattern, string, flags=0) 의 함수는 문자열의 시작 부분이 정규 표현식과 매칭되는지 확인한다.

string1 = "2017 december "
string2 = "the world of wolfstreet"

result3 = re.match(r'\d+', string1)
print(result3)
print(result3.group())
result4 = re.match(r'\d+', string2)
print(result4)

#search(pattern, string, flag=0) 문자열의 일부분이 정규표현식과 매칭하는지 확인 가능
result5 = re.search(r"[a-z]+", '777 how 132 are !!* you ???')
print(result5)

result6 = re.search(r"[A-Z]+", "hello my Name Is GoodBoyS")
print(result6)


#findall 부합하는 모든 문자열을 list 형태로 반환해준다.
result7 = re.findall(r"[a-z]+", "my Money name is WOLRD MONey")
print(result7)

#sub 의 경우에는 sub(pattenrs, changeStr, string, flags=0)
string3 = "my phone number is 010 - 7777 - 6666 , nice to meeet you"

result8 = re.sub(r'\d+', "xxxx", string3)
print(result8)

regex = re.compile(r'(\d+)-(\d+)-(\d+)')

phoneNum = regex.match('010-1111-1421')

print(phoneNum.group())
print(phoneNum.group(1))


regex1 = re.compile(r'(?P<first>\w+) (?P<last>\w+)')

names = regex1.match('minsoo k is people')

print(names.groups())
print(names.group(0))
print(names.group('first'))
print(names.group('last'))
print(names.groupdict())
print(names.expand(r'last: \1'))
print(names.expand(r'\2'))