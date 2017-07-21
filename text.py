def unicode_test(value):
    import unicodedata
    name = unicodedata.name(value)
    value2 = unicodedata.lookup(name)
    print('value="%s", name = "%s", value2="%s"' % (value, name, value2))

#unicode_test('A')
#unicode_test('$')


# unicode_test('\u20ac')
# unicode_test('\u2603')
# #unicode_test('Café')
# plcae = 'Café'
# print(plcae)


# pl = '\u00e9'.encode('utf-8')
# print(type(pl))
# place = 'caf\u00e9'
# print(type(place))
# print(place)

snowman = '\u2603'
print(len(snowman))
#print(snowman)
#print(snowman.encode('utf-8'))
print(len(snowman.encode('utf-8')))
