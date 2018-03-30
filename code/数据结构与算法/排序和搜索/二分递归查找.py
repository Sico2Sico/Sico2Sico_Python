#coding=utf-8

def binary_search(alist,item):

    if len(alist) == 0:
        return False

    else:
        midPoint = len(alist)//2

        if alist[midPoint] == item:
            return  True

        elif alist[midPoint] < item:
            binary_search(alist[midPoint+1:],item)

        else:
            binary_search(alist[:midPoint-1],item)

    return False

testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
print(binary_search(testlist, 3))
print(binary_search(testlist, 13))
