from greenlet import greenlet
import time


# 通过switch实现协程
def test1():
    while True:
        print("test1")
        gr2.switch()
        time.sleep(1)


def test2():
    while True:
        print("test2")
        gr1.switch()
        time.sleep(1)


gr1 = greenlet(test1)
gr2 = greenlet(test2)
gr1.switch()
