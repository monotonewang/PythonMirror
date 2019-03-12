import time
import random
from greenlet import greenlet

# 协程
# 使用yield 实现多任务
def task1():
    while True:
        t_start = time.time()
        time.sleep(random.random() / 2)
        t_end = time.time()
        print("task1 %0.2f" % (t_end - t_start))
        # time.sleep(1)

        # print("task1")
        yield


def task2():
    while True:
        t_start = time.time()
        time.sleep(random.random() / 2)
        t_end = time.time()
        print("task2 %0.2f" % (t_end - t_start))
        # time.sleep(1)
        # print("task2")
        yield


def main():
    # g1 = greenlet(task1)  # 创建协程g1
    # g2 = greenlet(task2)
    #
    # g1.switch()  # 跳转至协程g1

    t1 = task1()
    t2 = task2()

    count = 0
    while count < 10:
        count += 1
        next(t1)
        next(t2)


# while True:
#     task1()
#     task2()


if __name__ == '__main__':
    main()
