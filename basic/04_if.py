import random

age = 18

if age > 18:
    print(" more than 18")
else:
    print("less than 18")

#  if elif 语法-两种课程成绩

c_score = 50
p_score = 70
if c_score > 60 and p_score > 60:
    print("good")
else:
    print("bad")

if c_score > 60 or p_score > 60:
    if c_score > 60:
        print("c_score good")
    elif p_score > 60:
        print("p_score good")
else:
    print("bad")

# //随机函数使用
computer = random.randint(1, 3)

print(computer)



