number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#print(number.pop(5))
#print(number)
#del number[5]
#print(number)
#print(number.remove(3))
#print(number)
#number_1 = [5, 4, 3, 2, 1]
#number_1.remove(1)
#print(number_1)

##number = [] 초기화/전체삭제
##pop 은 리스트 인덱스의 해당 값을 뽑고나서 삭제(print 출력시 해당 데이터 나옴)
##DEL 은 리스트 인덱스의 해당값 삭제
##remove() 인자값 ::  해당 인덱스 값이 아닌 리스트 상의 해당 인자값을 삭제

number_2 = [1,2,3,7,1,1,4,2,1]
##리스트 상의 요소의 갯수 세기
#print(number_2.count(1))
setNumber = set(number_2)
for i in setNumber:
    print('{0} 에 갯수 ::: {1}'.format(i, number_2.count(i)))


num = [x for x in range(10) if x % 2]
print(num)