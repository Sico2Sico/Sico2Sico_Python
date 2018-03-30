#coding=utf-8

class Node(object):
    def __init__(self, elem =-1, lchild = None,rchild= None):
        self.elem = elem
        self.lchild = lchild
        self.rchild = rchild




class Tree(object):

    def __init__(self,root=None):
        self.root = root



    def add(self,elem):
        node = None(elem)

        if self.root == None:
            self.root = node

        else:

            queue = []

            queue.append(self.root)

            while queue:
                cur = queue.pop()

                if cur.lchild == None:
                    cur.lchild =node
                    return
                elif cur.rchild == None:
                    cur.rchild = node
                    return
                else:

                    queue.append(cur.lchild)
                    queue.append(cur.rchild)


    #先序遍历
    def preorder(self,root):

        if root == None :
            return
        print(root.elem)
        self.preorder(root.lchild)
        self.preorder(root.rchild)


    #中序遍历
    def inorder(self,root):

        if root == None:
            return

        self.inorder(root.lchild)
        print(root.elem)
        self.inorder(root.rchild)


    #后序遍历
    def postorder(self,root):

        if root == None:
            return

        self.postorder(root.lchild)
        self.postorder(root.rchild)
        print(root.elem)
