# 生成器是一种特殊的迭代器
def create_nums(all_num):
    a, b = 0, 1
    current_num = 0
    while current_num < all_num:
        yield a  # 如果里面有yield语句，那么这个不再是函数，就是一个生成器模板。
        a, b = b, a + b
        current_num += 1
    pass


if __name__ == '__main__':
    # 如果里面有yield，那么不再是调用函数，那么是创建一个生成器对象
    for num in create_nums(10):
        print(num)

    obj = create_nums(10)
    ret = next(obj)
    print(ret)
