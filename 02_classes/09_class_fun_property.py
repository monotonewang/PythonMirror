class Foo:
    def get_attr(self):
        return "laowang"
    

    BAR=property(get_attr)

obj=Foo()
result=obj.BAR  #通过调用属性的方法获取到方法的返回值
print(result)
print(obj.BAR.__doc__) # 获取该属性的描述信息
print(obj.__module__) # 获取该对象属于哪个模块
print(obj.__class__) # 获取该对象属于哪个类