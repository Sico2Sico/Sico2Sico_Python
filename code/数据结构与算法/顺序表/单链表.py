#coding=utf-8

class SingleNode(object):

    def __init__(self,item):
        self.item = item
        self.next = None




class SingleLinkList(object):
    def __init__(self):
        self._head = None

    #判断list是否为nil

    def is_empty(self):
        return  self._head == None


    # 获取list的长度
    def length(self):
        cur = self._head
        count = 0

        while cur != None:
            count += 1
            cur = cur.next
        return  count


    #遍历list
    def travel(self):
        cur = self._head
        while cur != None:
            print("cur = %d",cur.item)
            cur = cur.next
        print("")


    #头部添加
    def add(self,item):
        node = SingleNode(item)
        node.next = self._head
        self._head = node


    #尾部添加
    def append(self,item):
         node = SingleNode(item)

         if self.is_empty():
             self._head = node

         else:
            cur = self._head

            while cur.next != None:
                cur = cur.next
            cur.next = node

    #插入指定位置
    def insert(self,pos,item):

        if pos <= 0:
            self.add(item)
        elif pos > (self.length()-1):
            self.append(item)
        else:

            node = SingleNode(item)
            count = 0

            pre = self._head
            while count < (pos -1):
                count +=1
                pre = pre.next
            node.next = pre.next
            pre.next = node



    #移除指定的value
    def remove(self,item):
        cur = self._head
        pre = None

        while cur != None:

            if cur.item  == item:
                if not pre:
                    self._head = cur.next
                else:
                    pre.next = cur.next
                break

            else:
                pre = cur
                cur = cur.next



    #搜索是否存在
    def search(self,item):
        cur = self._head
        while cur != None:
            if cur == item:
                return  True
            cur = cur.next

        return  False



if __name__ == "__main__":

    ll = SingleLinkList()

    ll.add(1)
    ll.add(2)
    ll.append(3)
    ll.insert(2, 4)
    #
    ll.travel()

    ll.remove(1)

    ll.travel()

    print("end")