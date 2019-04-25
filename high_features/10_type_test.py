class Person(object):
    def eat(self,food='rice'):
        print("eat %s " % food)

p=Person()
p.eat(food="apple")


# 通过type创建对象的方式。 在创建数据库的时候需要用到
def eats(self,food='rice'):
    print("eats %s " % food)

People2=type("People",(object,),{"eat":eats})
p2=People2()
p2.eat()

print(type(p2))
# type就是元类
print(type(People2))
