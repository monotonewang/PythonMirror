class Women:
    def __init__(self, name):
        self.name = name
        self.__age = 19

    def __secret(self):
        # 对象的方法内部,可以范围对象的私有属性
        print("私有方法 age is %d,name is  %s" % (self.__age, self.name))

    def getAge(self):
        print("公有方法 getAge is %d" % self.__age)


women = Women("lili")
print(women.name)
# 私有属性， 在外界不能够直接访问
print(women._Women__age)
# 私有方法，同样不可以被外界直接访问
print(women._Women__secret())

# 通过调用父类公用方法 间接访问私有属性
print(women.getAge())


pass
