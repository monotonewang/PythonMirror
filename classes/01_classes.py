class Cat:
    def eat(self):
        print("%s cat eat" % self.name)


cat = Cat()
# 设置属性
cat.name = "tom"
cat.eat()
# print(cat.name)
print(cat)
print(id(cat))
