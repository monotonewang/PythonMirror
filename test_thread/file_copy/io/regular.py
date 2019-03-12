import re

# 正数和负数
regEx = "^(\\-|\\+)?\\d+(\\.\\d{1,2})?$"
test = "12121212"
result = re.match(regEx, test)  # 判断用户返回值
test1 = result.group()

print(test1)

print(result)
