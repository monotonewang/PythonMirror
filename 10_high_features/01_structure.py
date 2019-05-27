from collections import Iterable

# 如何判断一个对象是可迭代对象呢？
print(isinstance('collections.abc', Iterable))

# 如果要对list实现类似Java那样的下标循环怎么办？Python内置的enumerate函数可以把一个list变成索引-元素对，这样就可以在for循环中同时迭代索引和元素本身
for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)

print("numberList below")
numberList = [(1, 1), (2, 4), (3, 9)]
for x, y in numberList:
    print(x, y)

L = []
n = 1
while n <= 99:
    L.append(n)
    n = n + 2

print(L)

# 切片
print(L[0:3])

list = list(range(100))

print(list)

# 取偶数
print(list[::2])

# java
# /*    List<Integer> list = new ArrayList<>();
#
#         int a = 1;
#         while (a <= 99) {
#             list.add(a);
#             a = a + 2;
#         }*/
