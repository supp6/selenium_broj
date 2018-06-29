# coding=utf-8
import time
'''装饰器的使用：带参数的装饰器的使用'''

def timer(parameter):

    def outer_deco(func):
        print('in the outer_wrapper:',parameter)

        def deco(*args,**kwargs):
            if parameter=='task1':
                start=time.time()
                result=func(*args,**kwargs)     #为了使程序更加有扩展性，装饰器中使用了可变参数
                stop=time.time()
                print('the task1 run time is:',stop-start)
                return result
            elif parameter=='task2':
                start=time.time()
                result=func(*args,**kwargs)
                stop=time.time()
                print("the task2 run time is:",stop-start)

        return deco
    return outer_deco


@timer(parameter='task1')           # 装饰器带上参数，告诉装饰器是哪个
def task1(a=3,b=8):
    time.sleep(2)
    print("装饰器装饰的函数有返回结果情况，函数结果：")
    r=a+b
    return r

@timer(parameter='task2')
def task2():
    time.sleep(3)
    print('in the task2')

#函数的调用
task1(5,9)
task2()