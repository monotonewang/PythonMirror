# python 导入模块 as是别名

import classes.module_import.personZ as personQ

import classes.module_import.dog as myDog

# 局部导入
from classes.module_import.cat import smile

# 猫类和狗类 都有 smile 方法 同名工具
from classes.module_import.dog import smile as dog_smile

import classes.test_import.send_message as se_message
import classes.test_import.receiver_message as re_message

# 使用绝对路径来导入模块

re_message.receive()
se_message.send()

myDog.eat()

smile()

dog_smile()

personQ.run()
dog = personQ.Dog("awang")
dog.run()

# 模块搜索顺序,路径
print(personQ.__file__)

# 查看当前运行的方法--->__main__
print(__name__)
print(dog)
