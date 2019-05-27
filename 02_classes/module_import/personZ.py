# 只有运行为主程序才会执行后续代码
# if __name__ == "__main__":
class Dog:
    def __init__(self, name):
        self.name = name
        print("person play with %s" % self.name)

    def run(self):
        print("person run with %s" % self.name)

    pass


def run():
    print("person run")


print(" i am person Z")
