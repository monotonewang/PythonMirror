# 锁'

import threading
import time

g_num = 0

mutex = threading.Lock()


def count1(number, max):
    global g_num

    if mutex.acquire():
        print("count1= max %d %d" % (g_num, max))
        for i in range(max):
            g_num += 1
        mutex.release()
        print("count1=%d" % g_num)


def count2(number, max):
    global g_num
    if mutex.acquire():
        for i in range(max):
            g_num += 1
    mutex.release()
    print("count2=%d" % g_num)


def main():
    number = [10, 20]
    max = 10000000
    thread = threading.Thread(target=count1, args=(number, max,))
    thread1 = threading.Thread(target=count2, args=(number, max,))
    thread.start()
    thread1.start()

    time.sleep(5)

    print("main=%d" % g_num)

    print("number in main thread=%s" % str(number))


if __name__ == '__main__':
    main()
