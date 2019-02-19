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


print(count(1, 2))
