# class Duck():
#     def __init__(self, input_name):
#         self.hidden_name = input_name
#     def get_name(self):
#         print('inside the getter')
#         return self.hidden_name
#     def set_name(self, input_name):
#         print('inside the setter')
#         self.hidden_name = input_name
#     name = property(get_name, set_name)
#
#
# fowl = Duck('howorld')
# print(fowl.name)
# #print(fowl.get_name())


class Duck():
    def __init__(self, input_name):
        self.hidden_name = input_name

    @property
    def name(self):
        print('inside the getter')
        return self.hidden_name

    @name.setter
    def name(self, input_name):
        print('inside the setter')
        self.hidden_name = input_name


fowl = Duck('harwoid')
#print(fowl.hidden_name)
fowl.name = 'donald'
#print(fowl.name)


class Circle():
    def __init__(self, radius):
        self.radius = radius
    @property
    def diameter(self):
        return 2 * self.radius

cr = Circle(5)
#print(cr.radius)
#print(cr.diameter)
cr.radius = 8
#print(cr.diameter)


class DuckV2():
    def __init__(self, input_name):
        self.__name = input_name
