#coding=utf-8

class Stack(object):
    def __init__(self):
        self.items= []


    def is_empty(self):
        return self.items == []

    def push(self,item):
        self.items.append(item)

    def pop(self):
        self.items.pop()

    def peek(self):
        return self.items[len(self.items) -1]

    def size(self):
        return  len(self.items)




if __name__ == "__main__":
    stack = Stack()
    stack.push("hello")
    stack.push("world")
    stack.push("itcast")
    print("end")
