import _thread

import threading
import time

g_num = 0


# thread args参数可以实现共享
def test1(number, max):
    # number.append(30)
    # time.sleep(1)
    # number.append(40)
    # print("test=%s" % str(number))
    global g_num
    for i in range(max):
        g_num += 1
    print("test=%d" % g_num)


def test2(number, max):
    global g_num
    # print("test=%s" % str(number))

    for i in range(max):
        g_num += 1
    print("test1=%d" % g_num)


# 多线程共享参数 变量同步问题 次数越大，出问题的可能性 越大。次数越小，出问题的可能性越小
# count1= max 0 1000000
# count1=1230920count2=1279468
# main=1279468

def count1(number, max):
    global g_num
    print("count1= max %d %d" % (g_num, max))
    for i in range(max):
        g_num += 1
    print("count1=%d" % g_num)


def count2(number, max):
    global g_num

    for i in range(max):
        g_num += 1
    print("count2=%d" % g_num)


def main():
    number = [10, 20]
    max = 10000
    thread = threading.Thread(target=test1, args=(number, max,))
    thread1 = threading.Thread(target=test2, args=(number, max,))
    thread.start()
    thread1.start()

    time.sleep(5)

    print("main=%d" % g_num)

    print("number in main thread=%s" % str(number))


if __name__ == "__main__":
    main()
