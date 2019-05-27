txt = open('word.txt')
# 一次性读写消耗内存
text = txt.read()
print(txt)
print(text)
print(len(text))


# 复制文件
file2 = open("b.txt", "w")
file2.write(text)
file2.close()

print("-" * 20)
