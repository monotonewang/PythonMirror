list1 = ['physics', 14, '1', 121.12]

print(list1[0])

# 切片
print(list1[0:3])

list1.append("beijing")
print(list1.__len__())
print(list1[list1.__len__()-1])
list1.reverse()
print(list1[0:list1.__len__()-1])

print(list1.__sizeof__())

