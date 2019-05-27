txt = open('word.txt')
# 一次性读写消耗内存
text = txt.read()
print(txt)
print(text)
print(len(text))

print("-" * 20)

# 由于文件指针移动到最后，所以第二次无法读取到内容了
text1 = txt.read()
print("第二次读取 %s" % text1)
print()
# 使用完文件一定要关闭
txt.close()


# 消耗内存小
def read_line():
    print("begin read_line")

    txt = open('word.txt')

    while True:
        text = txt.readline()

        if not text:
            break
        print(text, end="")
        # 使用完文件一定要关闭
    txt.close()


read_line()
