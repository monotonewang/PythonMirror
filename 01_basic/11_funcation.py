import math


def say():
    print("who say")


# 方法可以独立定义
say()

# python 使用 lambda 来创建匿名函数。

sum = lambda arg1, arg2: arg1 + arg2

print(sum(10, 20))

"""
定义有参的函数
"""


def count(a, b):
    return a + b


# 一个函数返回多个值 其实返回的是tuple 元组
def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny


# 传入一个list，添加一个END再返回
def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L


#  可变参数
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum


#  关键字参数  关键字参数有什么用？它可以扩展函数的功能。
def person(name, age, **kw):
    if 'city' in kw:
        print("city-is")
        pass
    print('name:', name, 'age:', age, 'other:', kw)


#  关键字参数  限制关键字参数 参数是必填的
def personCity(name, age, *, city, job):
    print(name, age, city, job)


print(count(1, 2))

print(calc(1, 2, ))
print(calc(1, 2, 3))

print("person", person("bob", 1))

print("person", person("bob", 1, city='beijing'))

print("personCity",personCity("jim",1,city="shanghai",job='teacher'))
list = [1, 2, "2"]
listTemp = add_end(list)
print(listTemp)
x, y = move(1, 2, 2, 3)
print("x= y=", x, y)
print(abs(-20))

# *args：（表示的就是将实参中按照位置传值，多出来的值都给args，且以元组的方式呈现）
def foo(x ,*args):
    print(x)
    print(args)

foo(1,2,3,4,5)

# 当args与位置参数和默认参数混用的情况下：（注意三者的顺序）
def foo1(x,*args,y=1):
    print(x)
    print(args)
    print(y)

foo1(1,2,3,4,5)

# **kwargs：（表示的就是形参中按照关键字传值把多余的传值以字典的方式呈现）
def foo2(x,**k):
    print(x)
    print(k)

foo2(1,y=1,a=2)