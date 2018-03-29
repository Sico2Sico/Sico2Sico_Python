#coding=utf-8

from threading import  Thread
import time


g_unm = 100

def work1():
    global g_unm
    for i  in range(3):
        g_unm += 1

        print("_______in work1, g_unm==%d"%g_unm)



def work2():
    global  g_unm
    print("----in work2, g_num is %d---" % g_unm)



print("创建线程前======g_unm %d"%g_unm)


t1 = Thread(target=work1())
t1.start()

time.sleep(1)


t2 = Thread(target=work2())

t2.start()

