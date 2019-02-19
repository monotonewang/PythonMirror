a = 1
sum = 0
while a <= 100:

    if a > 99:
        break
    if a == 2:  # 2 不处理
        a = a + 1
        continue
    else:
        sum = sum + a
        a = a + 1

#  去掉默认的换行
print("*", end="")
print(sum)

# 打印小星星
line = 0
while line <= 5:
    print("*" * line)
    line = line + 1

column = 1
row = 1
while row <= 9:
    column = 1
    while column <= row:
        # print("%d * %d" % (row, column))
        # row=row+1
        # /t 文本在垂直方向对齐
        print("%d * %d = %d" % (row, column, row * column), end="\t")
        column = column + 1
    row = row + 1

    print("")
