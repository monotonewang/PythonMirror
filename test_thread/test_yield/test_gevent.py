import gevent
import time

from gevent import monkey

# 如果要使用time.sleep 需要使用monkey.patch_all
monkey.patch_all()


def f(n):
    for i in range(n):
        print(gevent.getcurrent(), i)
        # time.sleep(0.1)
        gevent.sleep(1)  # 要让greenlet交替运行，可以通过gevent.sleep()交出控制权：


g1 = gevent.spawn(f, 5)
g2 = gevent.spawn(f, 5)
g3 = gevent.spawn(f, 5)

g1.join()
g2.join()
g3.join()

# normal:
# <Greenlet at 0x10e6f7488: f(5)> 0
# <Greenlet at 0x10e6f7488: f(5)> 1
# <Greenlet at 0x10e6f7488: f(5)> 2
# <Greenlet at 0x10e6f7488: f(5)> 3
# <Greenlet at 0x10e6f7488: f(5)> 4
# <Greenlet at 0x10e6f7598: f(5)> 0
# <Greenlet at 0x10e6f7598: f(5)> 1
# <Greenlet at 0x10e6f7598: f(5)> 2
# <Greenlet at 0x10e6f7598: f(5)> 3
# <Greenlet at 0x10e6f7598: f(5)> 4
# <Greenlet at 0x10e6f76a8: f(5)> 0
# <Greenlet at 0x10e6f76a8: f(5)> 1
# <Greenlet at 0x10e6f76a8: f(5)> 2
# <Greenlet at 0x10e6f76a8: f(5)> 3
# <Greenlet at 0x10e6f76a8: f(5)> 4


# gevent.sleep(1)
# result:
# <Greenlet at 0x1055fe488: f(5)> 0
# <Greenlet at 0x1055fe598: f(5)> 0
# <Greenlet at 0x1055fe6a8: f(5)> 0
# <Greenlet at 0x1055fe488: f(5)> 1
# <Greenlet at 0x1055fe598: f(5)> 1
# <Greenlet at 0x1055fe6a8: f(5)> 1
# <Greenlet at 0x1055fe488: f(5)> 2
# <Greenlet at 0x1055fe598: f(5)> 2
# <Greenlet at 0x1055fe6a8: f(5)> 2
# <Greenlet at 0x1055fe488: f(5)> 3
# <Greenlet at 0x1055fe598: f(5)> 3
# <Greenlet at 0x1055fe6a8: f(5)> 3
# <Greenlet at 0x1055fe488: f(5)> 4
# <Greenlet at 0x1055fe598: f(5)> 4
# <Greenlet at 0x1055fe6a8: f(5)> 4
