try:
    a = 1 / 0
    num = int("xdfdafsf1221")
except ZeroDivisionError:
    print("exception")

# 捕获未知错误
try:
    b = 1
    # a = 1 / 0
    # num = int("xdfdafsf1221")
except Exception as result:
    print("exception %s" % result)
else:
    print("run else ")
finally:
    print("end ")


# 异常的传递
def count(a):
    if a<-1:
        ex =Exception("num is smaller")
        # 抛出异常
        raise ex
    return 1 / a

try:
    count(-2)
except Exception as result:
    print("count %s" % result)
finally:
    print("finally")
