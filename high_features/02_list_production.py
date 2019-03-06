def main():
    print(list(range(1, 11)))
    L = []

    for x in range(1, 11):
        L.append(x * x)
    return L


if __name__ == '__main__':
    L = main()
    print(L)
    # 而列表生成式则可以用一行语句代替循环生成上面的list：
    # list = [x * x for x in range(1, 11)]
    list = [x * x for x in range(1, 11) if x % 2 == 0]

    print(list)

    # 还可以使用两层循环，可以生成全排列
    print([m + n for m in 'ABC' for n in 'XYZ'])
