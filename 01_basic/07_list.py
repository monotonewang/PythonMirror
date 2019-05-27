list1 = ['physics', 14, '1', ['php', 1], 121.12]

fruits = ['Banana', 'Apple']

local_fruits = [fruit.upper() for fruit in fruits]

print("local_fruits=", local_fruits)

print(list1[0])

# 切片
print(list1[0:3])

list1.append("beijing")
print(list1.__len__())
print(list1[list1.__len__() - 1])
list1.reverse()
print(list1[0:list1.__len__() - 1])
print(list1[2][1])

print(list1.__sizeof__())

# ????---????append??????????????????
def extendList(val, list=[]):
    list.append(val)
    return list

list1 = extendList(10)
list2 = extendList(123,[])
list3 = extendList('a')

print ("list1 = %s" % list1)
print ("list2 = %s" % list2)
print ("list3 = %s" % list3)

def extendList2(val, list=None):
  if list is None:
    list = []
  list.append(val)
  return list

list11 = extendList2(10)
list21 = extendList2(123,[])
list31 = extendList2('a')

print ("list11 = %s" % list11)
print ("list21 = %s" % list21)
print ("list31 = %s" % list31)