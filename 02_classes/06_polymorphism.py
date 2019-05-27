class Person:

    def __init__(self, name):
        self.name = name

    def game_with_dog(self, dog):
        print("%s 和 %s 快乐的玩耍" % (self.name, dog.name))


class Dog:
    def __init__(self, name):
        self.name = name


class XiaoTianQuan(Dog):
    def __init__(self, name):
        self.name = name


# 父类
# dog = Dog("旺财")

# 子类
xiaotianquan = XiaoTianQuan("哮天犬")

person = Person("小明")

person.game_with_dog(xiaotianquan)
