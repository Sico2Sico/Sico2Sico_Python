#coding=utf-8

class Queue(object):
    def __init__(self):
        self.items = []


    #是否为空
    def is_empty(self):
        return  self.items == []

    #进队列
    def enqueue(self,item):
        self.items.insert(0,item)

    #出队列
    def dequeue(self):
        return  self.items.pop()

    #队列的大小
    def size(self):
        return  len(self.items)


if __name__ == "__main__":
    q = Queue()
    q.enqueue("hello")
    q.enqueue("world")
    q.enqueue("itcast")

    print("end")