#coding=utf-8

from time import  ctime,sleep

def timefun(func):

    def wrappedfunc():
        print("%s called at %s"%(func.__name__,ctime()))
        func()

    return wrappedfunc



def timefuncansu(func):
    def wrappedfunc(a,b):
        print("%s called at %s" % (func.__name__, ctime()))
        print(a, b)
        func(a,b)

    return wrappedfunc


@timefun
def foo():
    print("i am  foo")


@timefuncansu
def foo(a,b):
    print("i am  foo   a+b == %d"%(a+b))


print("-------------------------")
sleep(2)
foo(2,3)


