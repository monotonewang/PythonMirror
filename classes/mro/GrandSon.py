class Parent(object):
    def __init__(self, name):
        print("parent init start")
        self.name = name
        print("parent init end")


class Son1(Parent):
    def __init__(self, name, age):
        print("Son1 init start")
        self.age = age
        super().__init__(name)
        # Parent.__init__(name)
        print("Son1 init end")


class Son2(Parent):
    def __init__(self, name, gender):
        print("Son2 init start")
        self.gender = gender
        super().__init__(name)
        print("Son2 init end")


class GrandSon(Son1, Son2):
    def __init__(self, name, age, gender):
        # def __init__(self, name, age, gender):
        print("GrandSon init方法 start")
        super().__init__(name, gender)
        # Son1.__init__(self, name, age)
        super().__init__(name, age)
        # Son2.__init__(self, name, gender)
        print("GrandSon init方法 end")


# gs = GrandSon('gradson', 12, gender='boy')
gs = GrandSon('gradson', 12, 'boy')
# gs = GrandSon('gradson', 12,gender='1')
# print('name', gs.name)
# print('name', gs.age)
# print('name', gs.gender)
