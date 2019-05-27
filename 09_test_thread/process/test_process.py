import _thread

import multiprocessing
import threading
import time

# 共享全局变量
number = 1
max = 100


# python 多进程

def test():
    global number
    while number < max:
        number += 1
        print("test=%d" % number)
        pass


def test1():
    global number
    while number < max:
        number += 1
        time.sleep(1)
        print("test1=%d" % number)
        pass


def main():
    process1 = multiprocessing.Process(target=test)
    process2 = multiprocessing.Process(target=test1)
    process1.start()
    process2.start()
    time.sleep(2)

    print("main=%d" % number)

    # while True:
    #     length = len(threading.enumerate())
    #     print("current run thread %s" % length)
    #     if length <= 1:
    #         break


if __name__ == "__main__":
    main()
