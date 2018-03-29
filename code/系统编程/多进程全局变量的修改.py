#coding=utf-8
import os
import time

num = 0

pid = os.fork()

if pid == 0:
    num +=1
    print("num == %d"%num)
else:
    time.sleep(1)
    num +=1
    print("hahah2 ====%d"%num)


# 多进程中 每个进程中所有的数据(包括全局变量)都个拥有一份 互不影响
