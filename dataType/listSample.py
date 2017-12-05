



names = ['kim', 'tam billan', 'john', 'micky  del', 'albert', 'zidn']
#result1 = names.sort(key=len)

#sorted vs sort
result1 = sorted(names)
print(result1)
print('names 1 ', names)
# sort 의 경우 names 자체를 변경 후 none 반환
result2 = names.sort()
print(result2)
print('names 2', names)


names = ['kim', 'tam billan', 'john', 'micky  del', 'albert', 'zidn']
result3 = sorted(names, key=len, reverse=True)
print('result3 : ', result3)
print('names 3', names)
result4 = names.sort(key=len, reverse=True)
print('result4 : ', result4)
print('names 4', names)