import threading
import time


class my_thread(threading.Thread):
    def run(self):
        print("Starting %s" % self.name)



thread1 = my_thread(name="thread-1")
thread1.start()

