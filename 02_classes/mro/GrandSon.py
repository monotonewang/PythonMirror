class Parent(object):
    def __init__(self, name,*args,**kwargs):# 为避免多继承报错，使用不定长参数
        print("parent init start")
        self.name = name
        print("parent init end")


class Son1(Parent):
    def __init__(self, name, age,*args,**kwargs):
        print("Son1 init start")
        self.age = age
        super().__init__(name,*args,**kwargs)
        # Parent.__init__(name)
        print("Son1 init end")


class Son2(Parent):
    def __init__(self, name, gender,*args,**kwargs):
        print("Son2 init start")
        self.gender = gender
        super().__init__(name,*args,**kwargs)
        print("Son2 init end")


class GrandSon(Son1, Son2):
    def __init__(self, name, age, gender):
        # def __init__(self, name, age, gender):
        print("GrandSon init 开始调用 start")
        # super().__init__(name, gender)
        # Son1.__init__(self, name, age)
        # super().__init__(name, age)
        super().__init__(name, age,gender)
        # Son2.__init__(self, name, gender)
        print("GrandSon init 结束调用 end")


gs = GrandSon('gradson', 12, gender='boy')
gs = GrandSon('gradson', 12, 'boy')
# gs = GrandSon('gradson', 12,gender='1')
# print('name', gs.name)
# print('name', gs.age)
# print('name', gs.gender)
