#python 에서는 접근 지정자가 따로 있지 않다. 다만 암묵적 약속으로
# __abcde :; private
# _abcde :: protected

class Access:
    def __init__(self):
        self.public_field = 5
        self.__private_field = 10
        self._protected_field = 20

    def __private_method(self):
        print('private  method call')

class AccessV2:
    def __init__(self):
        self.alphabet = 'A'

    def set_alphabet(self,  alpha):
        self.alphabet = alpha
    def get_alphbat(self):
        return self.alphabet

class AccessV3:
    #property를 사용한 경우
    #get, set을 만들지 않고 간단하게 데이터를 접근을 하기위하여
    #변수를 set 할 경우 제한을 둘사 있다.
    def __init__(self):
        self.__alphabet = 'Z'

    @property
    def alphabet(self):
        return self.__alphabet

    @alphabet.setter
    def alphabet(self, alpha):
        # 변수를 set 할시 제한을 둘사 있다.
        if alpha not in ('A', 'B', 'C', 'D'):
            raise ValueError('Exception data')
        self.__alphabet = alpha

if __name__ == '__main__':
    ac = Access()
    ac.public_field = 1
    ac.__private_field = 2
    ac._protected_field = 3
    ##암묵적 약속임으로 출력시 변경된 데이터로 나온다.
    print(ac.public_field)
    print(ac.__private_field)
    print(ac._protected_field)

    # ac1 = AccessV2()
    # print(ac1.get_alphbat())
    # ac1.set_alphabet("B")
    # print(ac1.get_alphbat())

    ac3 = AccessV3()
    ac3.alphabet = 'J'
    print(ac3.alphabet)