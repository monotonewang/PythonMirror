
# 使用对象来实现方法的调用
# 缺点：为了计算多条线的值，需要对象中保存多个x,y值，浪费资源。


class Line5():
    def __init__(self, a, b):
       self.a = a
       self.b = b
    # 对象后面加括号，自动触发调用
    def __call__(self, temp):
        return (self.a+self.b)*temp


line5 = Line5(1, 2)
print("class1=%d" % line5(1))
print("class2=%d" % line5(2))

# 闭包


def ExFunc(x, y):
    def InsFunc(temp):
        return (x+y)*temp
    return InsFunc


myFunc = ExFunc(1, 2)
print(myFunc(1))
print(myFunc(2))

# 匿名函数能够完成简单的功能，传递是这个函数的引用，只有功能
# 普通函数能够完成较复杂的功能，传递的这个函数的引用，只有功能
# 闭包能够完成比较复杂的功能，传递是这个闭包中的函数以及数据，因此传递功能+数据
# 对象那个能够完成最为复杂的功能，传递很多数据和很多功能，因此传递功能+数据


# https://www.cnblogs.com/z360519549/p/5172020.html
# python引用变量的顺序： 当前作用域局部变量->外层作用域变量->当前模块中的全局变量->python内置变量 。

# nonlocal关键字用来在函数或其他作用域中使用外层(非全局)变量。
x = 300


def test1():
    x = 200

    def test2():
        nonlocal x
        print("xxxxxxxxxxxxxxxx1 %d" % x)
        x = 100
        print("xxxxxxxxxxxxxxxx2 %d" % x)
    return test2


t1 = test1()
t1()
