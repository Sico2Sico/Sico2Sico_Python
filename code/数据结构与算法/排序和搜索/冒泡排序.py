#coding=utf-8

def bubble_sort(alist):
    for j in range(len(alist)-1,0,-1):
        for i in range(j):
            if alist[i] < alist[i+1]:
                alist[i],alist[i+1] = alist[i+1],alist[i]





def dezzhibubble_srot(alist):

    count  = 0
    for j in range(len(alist)-1):

        for i in range(len(alist) -j -1):
            if alist[i] < alist[i + 1]:
                alist[i], alist[i + 1] = alist[i + 1], alist[i]




li = [54,26,93,17,77,31,44,55,20]
bubble_sort(li)
print(li)

print("===================")

li = [54,26,93,17,77,31,44,55,20]
dezzhibubble_srot(li)
print(li)