
print('=================9==================')
class Calc:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def sub(a, b):
        return a -b

    @staticmethod
    def mul(a, b):
        return a * b

    @staticmethod
    def div(a, b):
        return a / b
result1 = Calc.add(5, 8)
#print(result1)

result2 = Calc.div(6, 3)
#print(result2)