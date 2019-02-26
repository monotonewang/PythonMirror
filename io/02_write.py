# python 读取文件方式 默认 r 只读,
# w是写操作，如果文件不存在会创建
# a是追加模式，如果文件存在会将指针移动到文件末尾

file = open("mytxt.txt", 'w')
file.write("我是🇭🇰香港铜锣湾小哥")
file.close()
