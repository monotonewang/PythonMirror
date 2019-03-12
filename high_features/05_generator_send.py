def create_num(all_num):
    a, b = 0, 1
    num = 0
    while num < all_num:
        ret = yield a
        print(">>>", ret)
        a, b = b, a + b
        num += 1


obj = create_num(10)

ret = next(obj)
print(ret)

ret = obj.send("haha")  # 此时 等于前面的  yield a
print(ret)
