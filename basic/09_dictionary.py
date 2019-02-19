dic = {'a': 1, 'b': 2, "c": 3, 'd': 5}

print(dic['a'])
dic['a'] = 4

print(dic)

del dic['b']

# 随机返回并删除字典中的一对键和值。
dic.popitem()

print(dic)
print(dic.keys())
print(dic.values())

print(dic.__len__())
dic.clear()
print(dic)
