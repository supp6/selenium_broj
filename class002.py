# coding=utf-8
import time
'''装饰器的使用学习'''

def timer(func):
    def deco(*args, **kwargs):
        start=time.time()
        result=func(*args,**kwargs)     #为了使程序更加有扩展性，装饰器中使用了可变参数
        stop=time.time()
        print(stop-start)
        return result
    return deco

@timer           # 函数前加上装饰器，就可以实现装饰作用
def test(a=3,b=8):
    time.sleep(2)
    print("装饰器装饰的函数有返回结果情况，函数结果：")
    r=a+b
    return r


test(5,9)