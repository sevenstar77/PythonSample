def add_function(x):
    return x + 1

result = tuple(map(add_function, [1, 2, 3, 3]))
#print(result)

print('=================1==================')
result2 = list(map(lambda x: x * 3, [1,2,3]))
#print(result2)

print('=================2==================')
y = 7
result3 = (lambda x : x + y)(5)
#print(result3)

print('=================3==================')
#even_number
x = [1,2,3,4,5,6,7,8,9,10]
result4 = list(map(lambda x:  'even_num' if x % 2 == 0 else x, x))
#print(result4)
print('=================4==================')

result5 = [i for i in x if i % 2 == 0 if i % 4 ==0 ]
#print(result5)

print('=================5==================')
y = [1, 2, 3, 4, 5]
z = [3, 6 , 9, 12, 15]
result6 = list(map(lambda y, z: y * z, y, z))
print(result6)

print('=================6==================')

n = [13, 22, 5, 76, 8, 9, 12, 28, 39]
result7 = set(filter(lambda x: x > 20 and x < 70, n))
print(result7)


