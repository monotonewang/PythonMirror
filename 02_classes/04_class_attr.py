class Tool:
    # 该属性属于类属性
    count = 0

    def __init__(self):
        Tool.count += 1

    # 类方法可以调用类属性
    @classmethod
    def say(cls):
        print("this is class method %d" % cls.count)


tools1 = Tool()
tools2 = Tool()
tools3 = Tool()

print(Tool.count)

# 虽然可以使用 对象的类属性获取count，但是不推荐

tools1.count = 99
print(tools1.count)

# 调用类属性方法

Tool.say()
tools1.say()
