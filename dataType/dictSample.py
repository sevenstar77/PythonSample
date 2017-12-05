
a = dict(first="bob", second="silva", fullName="bobsilva")
b = dict(zip(['first', 'second', 'fullName'], ['bob', 'silva', 'bobsilva']))
c = dict([("first", 'bob'), ('second', "silva"), ("fullName", "bobsilva")])
print(a == c == b )


fruits = [(1, 'apple'), (2, 'banana'), (3, 'kiwi')]
fruitsDict = { code : fruit for code, fruit in fruits}
print(type(fruitsDict))
print(fruits)


