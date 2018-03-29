#coding=utf-8
import os
import time

pid = os.fork()

if pid == 0:
    print("1")
    print(os.getpid())
else:
    print("2")
    print(os.getpid())


print("============")

pid = os.fork()
if pid == 0 :
    print("3")
    print(os.getpid())
else:
    print("4")
    print(os.getpid())
time.sleep(1)

