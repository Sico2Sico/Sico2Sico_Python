#coding=utf-8

from multiprocessing import Queue

q = Queue(3)
q.put("消息1")
q.put("消息2")
print("show1====%s"%(q.full()))
q.put("消息3")
print("show2====%s"%(q.full()))


try:
    q.put("消息5",True,2)
except:
    print("消息队列已满")

try:
    q.put_nowait("消息4")
except:
    print("消息队列已满")


if not q.full():
    q.put_nowait("消息4")

if not q.empty():
    for i in range(q.qsize()):
        print(q.get_nowait())


