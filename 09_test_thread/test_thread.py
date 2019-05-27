import _thread

import threading
import time

# 共享全局变量
number = 1


def print_time(thread_name, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print(threading.current_thread())
        listThread = threading.enumerate()
        for i in listThread:
            print("\t name=%s ident=%d %s" % (i.name, i.ident, i.isAlive()))
        print("active_count--%d" % threading.active_count())
        print("%s,%s count=%d" % (thread_name, time.ctime(time.time()), count))


max = 999999


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
    try:
        _thread.start_new_thread(print_time("Thread-2", 0.1))
    except Exception as result:
        pass
    finally:
        pass

    thread = threading.Thread(target=test)
    thread1 = threading.Thread(target=test1)
    thread.start()
    thread1.start()
    time.sleep(2)

    print("main=%d" % number)

    # while True:
    #     length = len(threading.enumerate())
    #     print("current run thread %s" % length)
    #     if length <= 1:
    #         break


if __name__ == "__main__":
    main()
