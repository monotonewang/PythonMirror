# 当需要创建大量进程的时候，可以使用 进程中的Pool
# 初始化 Pool可以指定最大的进程数

from multiprocessing import Pool
import os, time, random


def worker(msg):
    t_start = time.time()
    print("%s 当前的进程号为：%d" % (msg, os.getpid()))
    time.sleep(random.random() * 2)
    t_end = time.time()
    print(msg, "执行完毕 %0.2f" % (t_end - t_start))


def main():
    print('Parent process %s.' % os.getpid())
    po = Pool(3)
    for i in range(0, 10):
        # po.apply_async(worker, args=(i,))
        po.apply_async(worker, (i,))  # 上面和下面语句一致， 该语句表示要调用的目标。传递元组过去
        # 每次循环会空闲出来的子进程去调用目标
    print('Waiting for all subprocesses done...')
    po.close()  # 关闭进程池，关闭后不再接受新的东西
    po.join()  # 等待po中所有子进程执行完毕
    print('All subprocesses done.')


if __name__ == '__main__':
    main()
