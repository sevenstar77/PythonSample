print('=================1==================')
def first_function():
    str = 'function test'
    def inner_function():
        print(str)
    inner_function()

#first_function()
print('=================2==================')

def test():
    total = 0
    def add(a, b):
        nonlocal total # nonlocal test() 의 total 변수를 사용한다고 설정 / global 의 경우 무조건 전역변수를 사용
        total = total + a +  b
    add(1, 2)
    add(3, 4)
    print(total)
#test()
print('=================3==================')
def closure_test():
    a = 2
    b = 3
    def add(x):
        return (a * x) + b
    return add

close = closure_test()
#print(close(4))

print('=================4==================')
def closure_lambda():
    a = 5
    b = 7
    return lambda x : a * x + b

lam = closure_lambda()
#print(lam(15))


print('=================5==================')
class Person:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
    def profile(self):
        print('name : {} , age : {}, grade : {}'.format(self.name, self.age, self.grade))

# p1 = Person()
# p1.name='pinokio'
# p1.profile()
p2 = Person('minho', 22, 'A')
#p2.profile()

print('=================6==================')

class Person2:
    #__slots__ = ['name']
    def __init__(self, name, age, grade, mobile):
        self.name = name
        self.age = age
        self.grade = grade
        self.__mobile = mobile

    def profile(self):
        print('name : {} , age : {}, grade : {}, mobile : {}'.format(self.name, self.age, self.grade, self.__mobile))

    def set_mobile(self, mobile_no):
        self.__mobile = mobile_no

#p3 = Person2('soo', 40, 'B')
p4 = Person2('soo', 50, 'A', '010-555-33')
#print(p4.age)
p4.age = 20
#p4.profile()
p4.set_mobile('010-234-987')
#p4.profile()

print('=================7==================')
class Animal:
    species = []

    def add_species(self, specie):
        self.species.append(specie)

animal1 = Animal()
animal1.add_species('개과')
#print(animal1.species)
animal1.add_species('고양이과')
#print(animal1.species)

print('=================8==================')

class Animal_1():
    def __init__(self):
        self.species = []

    def add_species(self, species):
        self.species.append(species)

a1 = Animal_1()
a1.add_species('물고기')
a1.add_species('새')
print(a1.species)

a2 = Animal_1()
a2.add_species('개')

#print(a2.species)


print('=================10==================')