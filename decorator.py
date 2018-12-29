# -*- coding:utf-8 -*-
'''
Created on Dec 27, 2018

@author: xuyanli
'''

import time

'''
#1、定义个函数，被装饰函数
def test():
    time.sleep(2)
    print("testing is running") 
test() 
'''

'''
#2.1、函数“变量”（或“变量”函数）
x = 1
y = x
def test1():
    print("Do something")
    
test2 = lambda x:x*2  #没有命名的函数

print(test1)  #test1表示的是函数的内存地址 
test1()       #调用对在test这个地址上的内容，即函数
print(test2.__name__) #打印函数名称
print(test2(2)) 
'''

'''
#2.2高阶函数
#条件1：有函数作为参数传入
#条件2：有函数作为参数返回，有其中一条条件就是高阶函数
def test():
    time.sleep(2)
    print("test is running")
    
def deco(func): #函数作为实参传入，是高阶函数
    start = time.time()
    func()      #地址指向传入实参函数的内存地址
    print("打印func函数的名称：",func.__name__)
    stop = time.time()
    print(stop - start)
    
deco(test)  #这样修改了调用方式，应该保持调用方式test()
'''


'''
#2.3 嵌套函数
#函数只能调用和它同级别以及上级的变量或函数
def timer(func):
    def deco():   #这个函数不需要传入参数吗？下面func就可直接调用了? 内部函数可以直接引用外部函数参数
        start = time.time()
        func()
        print("打印func的地址：",func)
        stop = time.time()
        print(stop - start)
    print("打印deco的地址：",deco)
    return deco

#test = timer(test) #网上事例代码是放这里的，但是报错：NameError: name 'test' is not defined

@timer  #真正的装饰器。将下面的函数作为参数传入装饰器中，近而在不修改函数本身和调用方式的前提下新增功能。
def test():
    time.sleep(2)
    print("test is running")
    
#test = timer(test) #等号左边的函数名称换成其他也可以。当有真正的装饰器后就不需要这句了。
print("打印timer的地址：",timer)
print("打印新test的地址：",test)
test()
'''

'''
#4、装饰有参函数
def timer(func):
    def deco(*arg, **kwargs):
        start = time.time()
        res =func(*arg, **kwargs)
        print("打印func的地址：",func)
        stop =time.time()
        print(stop - start)
        return res  #有返回值的装饰器
    print("打印deco的地址：",deco)
    return deco
 
@timer    
def test(parameter):    #被装饰函数有参数
    time.sleep(2)
    print("test is running")
    print("parameter is:",parameter)
    return "Returned value" #被装饰函数有返回值
    
test(3)
print("打印新test的地址：",test)
'''


#带参数的装饰器
def timer(parameter = 'task1'): #装饰多个函数
    print("最外层函数")
    def outer_warapper(func):
        print("第2层函数")
        def wapper(*args, **kwargs):
            print("第3层函数")
            if parameter == 'task1':
                start = time.time()
                func(*args, **kwargs)
                print("打印func的名字：",func.__name__)
                stop = time.time()
                print("the task1 run time is :", stop-start)
            elif parameter == 'task2':
                start = time.time()
                func(*args, **kwargs)
                print("打印func的名字：",func)
                stop = time.time()
                print("the task2 run time is :", stop-start)
        print("打印wapper的名字：", wapper.__name__)
        return wapper
    print("打印outer_warapper的名字：", outer_warapper.__name__)
    return outer_warapper

@timer(parameter = 'task1')
def task1():
    time.sleep(2)
    print("in the task1")
    
@timer(parameter = 'task2')
def task2():
    time.sleep(2)
    print("in the task2")

  
task1()
print("打印新task1的名字：", task1.__name__)
task2()  
print("打印新task2的名字：", task2.__name__)                  

#函数调用的顺序还是没搞懂
    



    