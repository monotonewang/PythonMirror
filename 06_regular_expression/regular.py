import re

# 正数和负数
regEx = "^(\\-|\\+)?\\d+(\\.\\d{1,2})?$"
test = "12121212"
result = re.match(regEx, test)  # 判断用户返回值
# re.search(regEx,test); 查看出现次数是多少
# re.findall(regEx,test); 查看总共出现多少次
# re.sub(regEx,test); 将匹配到的进行替换
test1 = result.group()


# . 匹配单个字符
# [] 匹配列举字符
# \d 匹配数字0-9
# \D 匹配非数字，即不是数字
# \s 匹配空白，即空格，tab键
# \w 匹配单词字符a-z A-Z 0-9 _
# \W 匹配非单词字符

# . 匹配多个字符
# * 匹配前一个字符出现0次或者无限次，即可有可无
# + 匹配一个字符出现1次或者无限次，即至少有1次
# ？ 匹配前一个字符出现1次或者0次，即要么有1次，要么没有
# {m} 匹配前一个字符出现m次
# {m,n} 匹配前一个字符出现从m到n次

# 匹配开头和结尾
# ^ 开头
# $ 结尾
print(test1)

print(result)
