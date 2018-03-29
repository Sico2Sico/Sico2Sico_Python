#coding=utf-8

from  threading import  Thread
import time

g_num = 0


def test1():
    global  g_num
    for i in range(100000):
        g_num += 1

    print("------test1-----g_num=%d"%g_num)



def test2():
    global  g_num
    for i in range(100000):
        g_num += 1

    print("--------test2-------g_num%d"%g_num)



p1 = Thread(target=test1)
time.sleep(3)
p2 = Thread(target=test2)

print("========")
p1.start()
p2.start()

print("========g_unm %d"%g_num)