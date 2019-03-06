import _thread

import threading
import time


# thread args参数可以实现共享
def test(number):
    number.append(30)
    print("test=%s" % str(number))
    pass


def test1(number):
    print("test1=%s" % str(number))


def main():
    number = [10, 20]
    thread = threading.Thread(target=test, args=(number,))
    thread1 = threading.Thread(target=test1, args=(number,))
    thread.start()
    thread1.start()

    print("number in main thread=%s" % str(number))


if __name__ == "__main__":
    main()
