#coding=utf-8

from threading import Lock,Thread
import time

g_num = 0


def test1():
    global  g_num
    for i in range(100000):
        mutexFlag =mutex.acquire(True)

        if mutexFlag:
            g_num += 1
            mutex.release()
    print("---test1---g_num=%d" % g_num)



def test2():
    global  g_num
    for i in range(100000):
        mutexFlag = mutex.acquire(True)
        if mutexFlag:
            g_num += 1
            mutex.release()

    print("---test2---g_num=%d" % g_num)


mutex = Lock()

p1 = Thread(target=test1)

p1.start()


p2 = Thread(target=test2)
p2.start()

print("g_num=%d"%g_num)