from collections import Iterable


# 迭代器存储的是生成数据的方式，不是结果
#  占用极少的内存空间3
def main():
    test_obj = range(0, 10)
    print(test_obj)
    for i in test_obj:
        print(i)

    print(isinstance((12, 12), Iterable))
    print(isinstance([12, 12], Iterable))
    print(isinstance("12, 12", Iterable))
    print(isinstance(123, Iterable))
    pass


if __name__ == '__main__':
    main()
