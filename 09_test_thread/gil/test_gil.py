from ctypes import *
from threading import Thread

lib = cdll.loadLibrary("./xxx.so")

t = Thread(target=lib.method)
t.start()

# 死循环
while True:
    pass
