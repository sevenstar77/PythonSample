class Person:
    def __init__(self):
        print('Person __init__')
        self.height = 0
        self.weight = 0
        self.age = 0

    def speak(self):
        print('hello')

    def walk(self):
        print('walking')

class Fighter(Person):
    def __init__(self): # 생성하지 않을경우 자동으로 부모 class 의 init 을 물료 받게 된다.
        print('fighter __init__')
        self.height = 115
        self.weight = 40
        self.foot_size = 250
        super().__init__()

    def walk(self):
        super().walk() #method overriding
        print('stepping')
    def attack(self):
        print('attack!')

print(issubclass(Fighter, Person))

m1 = Fighter()
m1.attack()
m1.speak()

print(m1.height)
print(m1.age) # 자식 class 안에서 super().__init__() 호출하여야만 부모 클래스의 값을 사용
print(m1.foot_size)
print('-------------------------')
m1.walk()