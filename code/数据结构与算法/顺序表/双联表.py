#coding=utf-8

class Node(object):
    def __init__(self,item):
        self.item = item
        self.next = None
        self.prev = None





class DLinkList(object):
    def __init__(self):
        self._head = None

    #判断是否为空
    def is_empty(self):
        return  self._head == None


    #获取长度
    def length(self):

        cur = self._head
        count = 0

        while cur != None:
            count += 1
            cur = cur.next
        return  count


    #遍历列表
    def travel(self):
        cur = self._head
        while cur != None:
            print(cur.item)
            cur = cur.next
        print("")


    #头部添加
    def add(self,item):
        node = Node(item)

        if self.is_empty():
            self._head = node

        else:
            node.next = self._head
            self._head.prev = node
            self._head = node


    #尾部添加
    def append(self,item):
        node = Node(item)

        if self.is_empty():
            self._head = node

        else:
            cur = self._head
            while cur.next != None:
                cur = cur.next

            cur.next = node
            node.prev = cur


    #搜索
    def search(self,item):
        cur = self._head

        while cur != None:
            if cur.item == item:
                return  True
            else:
                cur = cur.next
        return  False


    #插入
    def insert(self,pos,item):

        if pos <= 0:
            self.add(item)
        elif pos > (self.length() - 1):
            self.append(item)
        else:
            node = Node(item)

            cur = self._head
            count = 0

            while count < (pos -1):
                count +=1
                cur = cur.next

            node.next = cur.next
            node.prev = cur

            cur.next.prev= node

            cur.next = node


    #移除
    def remove(self,item):

        if self.is_empty():
            return
        else:
            cur = self._head

            #如果是第一个的时候
            if cur.item == item:
                if cur.next == None:
                    self._head = None
                else:
                    cur.next.prev = None
                    self._head = cur.next
                return

            while cur != None:
                if cur.item == item:
                    cur.prev.next = cur.next
                    cur.next.prev = cur.prev
                    break

                cur = cur.next




if __name__ == "__main__":

    ll = DLinkList()
    ll.add(1)
    ll.add(2)
    ll.append(3)
    ll.insert(2, 4)
    ll.insert(4, 5)
    ll.insert(0, 6)

    ll.travel()

    ll.remove(1)
    ll.travel()

    print("end")


