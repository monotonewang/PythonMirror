# set内容不可重复
s = set({1, 2, 3})
s.add(3)
s.add(4)
s.add(0)

print(s)
# remove的是 key=3这个元素
s.remove(3)
print(s)
