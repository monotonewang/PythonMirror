import multiprocessing
from multiprocessing import Pool
import os, time, random


def worker(queue, old_folder_name, new_folder_name, file_name):
    time.sleep(random.random() * 2)
    print("模拟文件copy %s-->%s-->%s-->%d" % (old_folder_name, new_folder_name, file_name, os.getpid()))
    old_f = open(old_folder_name + "/" + file_name, 'r')
    content = old_f.read()
    old_f.close()

    new_f = open(new_folder_name + "/" + file_name, 'w')
    result_int = new_f.write(content)
    new_f.close()

    queue.put((file_name, result_int))
    # queue.put(file_name)
    pass


def main():
    # 获取用户输入的文件夹名称
    old_folder_name = input("请输入文件名称")

    # 列出文件夹里面所有的文件
    file_names = os.listdir(old_folder_name)

    # 创建一个新的文件夹

    new_folder_name = old_folder_name + "_copy"
    if os.path.exists(new_folder_name):
        print("exist")
        pass
    else:
        print("not exist")
        os.mkdir(new_folder_name)

    # 使用多进程打印出来old文件夹里面的所有文件
    po = Pool(3)

    queue = multiprocessing.Manager().Queue()

    print(old_folder_name)
    for file_name in file_names:
        po.apply_async(worker,
                       args=(queue, old_folder_name, new_folder_name, file_name))  # 上面和下面语句一致， 该语句表示要调用的目标。传递元组过去
    po.close()
    po.join()

    while True:
        # file_nameTemp = queue.get()
        file_nameTemp, reuslt_int = queue.get()

        print("file_nameTemp=%s int-->%d" % (file_nameTemp, reuslt_int))
        # print("file_nameTemp=%s " % (file_nameTemp))
        if queue.empty():
            break
    copy_ok_num = 0
    all_file_num = len(file_names)
    while True:
        copy_ok_num += 1

        print("process %0.2f" % (copy_ok_num / all_file_num * 100))
        if (copy_ok_num >= all_file_num):
            break
    print('All subprocesses done.')

    pass


if __name__ == '__main__':
    main()
