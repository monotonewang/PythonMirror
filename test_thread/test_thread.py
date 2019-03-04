import _thread

import threading
import time

number = 1


def print_time(thread_name, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print("%s,%s count=%d" % (thread_name, time.ctime(time.time()), count))


def test():
    global number
    while number < 100:
        number += 1
        print("test=%d" % number)
        pass


def test1():
    global number
    while number < 100:
        number += 1
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

    while True:
        length = len(threading.enumerate())
        print("current run thread %s" % length)
        if length <= 1:
            break


if __name__ == "__main__":
    main()
