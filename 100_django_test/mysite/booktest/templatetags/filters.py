# 自定义过滤器
from django.template import Library
import os

# create a object Library
register = Library()

# 判断是否是偶数


@register.filter
def mod(num):
    return num % 2 == 0

@register.filter
def multi(x,y):
    return x*y

# 参数最多是两个
@register.filter
def mod_divde(num,val):
    return num%val==0

@register.filter
def real_path(num):
    return os.path.realpath(__file__)