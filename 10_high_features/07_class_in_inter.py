# from collections import Iterable
# from collections import Iterator


class Classmates(object):
    def __init__(self):
        self.names = list()
        self.current_num = 0

    def add(self, name):
        self.names.append(name)

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_num < len(self.names):
            name_temp = self.names[self.current_num]
            self.current_num = self.current_num + 1
            return name_temp
        else:
            return StopIteration


def main():
    classmates = Classmates()
    classmates.add("张")
    classmates.add("小")
    classmates.add("房")

    print(classmates)
    classmates_iter = iter(classmates)
    print(classmates_iter)
    # next = classmates_iter.__next__()
    # next1 = classmates_iter.__next__()
    # next2 = classmates_iter.__next__()
    # next3 = classmates_iter.__next__()//超出 index会报错
    # print("xxx=" + next, "xxx=" + next1, "xxx=" + next2)

    print("--------------------")
    for name in classmates:
        if isinstance(name, str):  # 这里判断他是否是一个字符串
            print(name)


pass

if __name__ == '__main__':
    main()
