from itertools import count
import itertools

alpa_1 = ['a', 'b', 'c', 'd']
alpa_2 = ('e', 'f',  'g', 'h')
alpa_3 = ['i', 'a', 'k', 'l']

#chain :: 각 자료형을 묶어 줄수 있다.
print(list(itertools.chain(alpa_1, alpa_2, alpa_3)))
#set 의 경우 중복되는 데이터 가 있을 경우 제외하고 노출된다.
print(set(itertools.chain(alpa_1, alpa_2, alpa_3)))

