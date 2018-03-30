#coding=utf-8

def insert_sort(alist):

    n = len(alist)
    for i in range(1,n):
        if alist[i] < alist[i-1]:
            for j in range(i,0,-1):
                if alist[j] < alist[j-1]:
                    alist[j],alist[j-1] = alist[j-1],alist[j]




alist = [54,26,93,17,77,31,44,55,20]

insert_sort(alist)

print(alist)






