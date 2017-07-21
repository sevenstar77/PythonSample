import itertools

bierce = {
    "day" : "A period of twenty-four hour",
    "positive" : "mistaken at the top",
    "misfourtune" : "the kind of fourtune"
}
#
# print(bierce)

lol = [['a', 'b'], ['c', 'd'], ['e', 'f']]
lol = dict(lol)
# #print(lol)
#
# print(list(lol.items()))

signals = {'green' : 'go', 'yellow' : 'go faster', 'red' : 'smile for the camera'}
save_signals = signals
signals['blue'] = 'confuse everyone'
#print(save_signals)

hours = {
    (44.79, -91.32, 284) : 'My house',
    (33.55, -27.12, 13) : 'the White hourse'
}


#print(list(hours.items()))

# alpahbet = ''
# alpahbet += 'abcde'
# alpahbet += 'eeed'
# print(alpahbet)


# alphbet = 'abcde' + \
#     'hijklmn' + \
#     'eeeeee'
# #
# print(alphbet)

numbers = [1,3,5]
position = 0

# print(len((numbers)))
# while position < len(numbers):
#     print('position %s' % position)
#     number = numbers[position]
#     if number % 2 ==0:
#         print('Found even number', number)
#         break
#     position += 1
# else:
#     print('no except')


days = ['Monday', 'tuseday', 'wednesday']
fruits = ['bananan', 'orange', 'peach']
drinks = ['coffee', 'tea', 'beer']
desserts = ['tiramisu', 'ice cream', 'pie', 'chocolet']

# for day, fruits, drinks, desserts in zip(days, fruits, drinks, desserts):
#     print(day, fruits, drinks, desserts)


english = 'monday','tuseday','wednesday'
french = 'ludi', 'mardi','markiri'

# print(list((zip(english, french))))
# print(dict(zip(english, french)))

number_list = list(range(0, 6))
#print(number_list)

#print([i for i in range(0, 6)])


#print([number for number in range(1, 6)])

#print([number - 1 for number in range(1,6)])

#print([number for number in range(1, 6) if number % 2 == 1])

rows = range(1, 4)
cols = range(1, 3)
# for row in rows:
#     for col in cols:
        #print(row, col)


cells = [(row, col) for row in rows if row != 1 for col in cols if col == 1]
#print(cells)

word = 'letters'
letter_counts = {letter : word.count(letter) for letter in word }
#print(letter_counts)


number_ting = (number for number in range(1, 6))
# for number in number_ting:
#     print('number 1  %s ' % number)
#
# #print(list(number_ting))
#
# for number in number_ting:
#     print('number 2 %s' % number)
#
# def menu(wine, entree, dessert='pudding'):
#     return {'wine' : wine, 'entree' : entree, 'dessert' : desserts}
#
# def buggy(arg, result=[]):
#     result.append(arg)
#     print(result)


#aa = buggy('a')

#bb = buggy('b')
#print(bb)


# def document_it(func):
#     def new_function(*args, **kwargs):
#         print('Running function:', func.__name__)
#         print('Positional argument', args)
#         print('keyword arguments' , kwargs)
#         result = func(*args, **kwargs)
#         print('Result', result)
#         return result
#     return new_function
#
# def add_ints(a, b):
#     return a + b
#
# print(add_ints(5, 8))
#
# cooler_add_ints =  document_it(add_ints)
# cooler_add_ints(6, 5)
#
#
# @document_it
# def sub_ints(a, b):
#     return a - b
#
# sub_ints(16, 5)



quotes = {
    'Moe' : 'A wise guy, huh',
    'Larry' : 'Ow!',
    'Courly' : 'nyuk ny',
}


# for quote in quotes:
#     print(quote)
from collections import OrderedDict

quotesV = OrderedDict([
    ('Moe', 'a wiase'),
    ('kerry', 'bc8'),
    ('good', 'good man')
])


for qot in quotesV:
    print(qot)


def palindrome(word):
    from collections import deque
    dq = deque(word)
    while len(dq) > 1:
        if dq.popleft() !=dq.pop():
            return False
        return True

# print(palindrome('abcdf'))#
# print(palindrome('aba'))


for item in itertools.chain([1, 2], ['a', 'b']):
    print(item)

# for item in itertools.cycle([1, 2]):
#     print(item)


for item in itertools.accumulate([1,2,3,4]):
    print(item)