for letter in 'Python':
    print('current word', letter)

fruits = ['banana', 'apple', 'orange']
for fruit in fruits:
    print("noraml:" + fruit)

for i in range(0, 10):
    print("noraml:" + str(i))


def add(n, i):
    print("n"+str(n)+"i="+str(i))
    print("n+i      ="+str(n+i))
    return n+i

lis = [x*x for x in range(4)]
print(lis)

print("lis first xxxxxxxx i=:")
listx=(0,1,2,3)
listxy =(x*x for x in listx)
print(listx)
print(list(listxy))
print(listxy)

print("lis second  xxxxxxxx i=:")

# for i in gy:
# print("gy i=:" + str(i))
gy = [1, 1, 1]

for x in [1,2,1]:
    text = (x+i for i in gy)
    print("x"+str(x)+"i="+str(i))
    print(text)
    gy = text
print(list(gy))

# for x in [1, 2, 1]:
#     text = [x+i for i in gy]
#     print("x"+str(x)+"i="+str(i))
#     print(text)
#     gy = text
# print(list(gy))
