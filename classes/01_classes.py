class Cat:

    def __init__(self, height, weight):
        self.height = height
        self.weight = weight

    def eat(self):
        print("%s cat eat" % self.name)
        self.weight += 0.5  # 吃东西增加体重

    def __del__(self):
        print(" class is destory")

    def __str__(self):
        return "cat height __str__ %s weight %s" % (self.height, self.weight)


cat = Cat(12, 75)
# 设置属性
cat.name = "tom"
cat.eat()
# print(cat.name)
print(cat)
print(id(cat))

print(cat)
print(cat.__class__)
print(cat.height)

print(hasattr(cat, 'name'))

print(cat)

delattr(cat, 'height')  # 删除属性 'age'

del cat

print("the program is run end")
