def create_num(all_num):
    a, b = 0, 1
    current_num = 0
    while current_num < all_num:
        yield a  # 迭代器 和return类似
        a, b = b, a + b
        current_num += 1


obj2 = create_num(10)

ret = next(obj2)
print("ret="+str(ret))
ret2 = obj2.send(None)
print("ret2="+str(ret2))

# 可以使用for循环迭代输出
while True:
    try:
        ret = next(obj2)
        print(ret)
    except Exception as result:
        pass
#
# # 捕获未知错误
# try:
#     b = 1
#     # a = 1 / 0
#     # num = int("xdfdafsf1221")
# except Exception as result:
#     print("exception %s" % result)
# else:
#     print("run else ")
# finally:
#     print("end "
