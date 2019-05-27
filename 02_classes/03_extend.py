class Animal:
    def eat(self):
        print("animal eat")


class Dog(Animal):
    # def eat(self):
    #     print("dog eat")
    pass


class Cat(Animal):
    def eat(self):
        print("cat eat")
        # 通过super() 可以调用父类的方法
        super().eat()
        # 可以通过父类--调用方法--但是不推荐
        Animal.eat(self)

    pass


dog = Dog()

# 子类可以调用父类方法
dog.eat()

# 子类会重写父类方法
cat = Cat()
cat.eat()
