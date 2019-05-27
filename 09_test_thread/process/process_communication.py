import multiprocessing


def download_from_web(queue):
    # 下载数据
    data = [11, 22, 33, 44]
    for number in data:
        queue.put(number)
    pass


def analysis_data(queue):
    # 从队列中获取数据

    while True:
        data = queue.get()
        print(data)
        if queue.empty():  # 队列为空退出循环
            break
    pass


def main():
    queue = multiprocessing.Queue()

    p1 = multiprocessing.Process(target=download_from_web, args=(queue,))
    p2 = multiprocessing.Process(target=analysis_data, args=(queue,))
    p1.start()
    p2.start()
    pass


if __name__ == '__main__':
    main()
