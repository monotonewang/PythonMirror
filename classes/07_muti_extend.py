# python 支持多继承
class A(object):
    def play(self):
        print("a play")

    pass


class B(object):

    def play(self):
        print("b play")

    pass


# 优先会调用 A 的方法
class C(A, B):
    pass


c = C()
c.play()

print(c)
