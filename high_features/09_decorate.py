
def add_fun(func):
    print("add_fun start")
    def call_func(*args,**kwargs):
        print("this is add_fun call_func")
        return func(*args,**kwargs)
        print("this is add_fun call_func end")
    return call_func

#这里方法参数是函数的引用
def set_fun(func):
    print("set_fun start")
    def call_func(num,*args,**kwargs):
        print("this is  set_fun call_func")
        return func(num,*args,**kwargs)
        print("this is set_fun call_func end")
    return call_func

# 在执行之前已经被装饰
# 支持同时多个装饰器
@add_fun
@set_fun
def test1(num,*args,**kwargs):
    print("this is test1 method")
    return "ok";

# 这里改变了test1的指向，指向了 call_func 方法1 
test1 = set_fun(test1)
ret=test1(1)
print(ret)

# 方法2这是 装饰器写法
test1(1)

@set_fun
def test2(num,*args,**kwargs):
    print("下面是打印不定长参数：")
    print("this is test2 method %d" % num)
    print("this is test2 args ",args)
    print("this is test2 kwargs ",kwargs)
    return "ok";

test2(100)
test2(100,200)
test2(100,200,300,mm=101)

#  下面是带有参数的装饰器
def set_level(level_num):
    def set_fun(func):
        print("set_fun start")
        def call_func(num,*args,**kwargs):
            if(level_num==2):
                print("this is  set_fun call_func")
            else:
                print("level_num not == 1")
            return func(num,*args,**kwargs)
            print("this is set_fun call_func end")
        return call_func
    return set_fun

@set_level(1)
def l_test1(num,*args,**kwargs):
    print("this is level test")
    return "xx"

l_test1(1)
