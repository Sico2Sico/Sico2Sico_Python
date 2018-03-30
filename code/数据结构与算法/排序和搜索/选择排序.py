#coding=utf-8

def selection_srot(alist):

    n = len(alist)

    for i  in range(n-1):

        min_index = i

        for j in  range(i+1,n):
            if alist[min_index] < alist[j]:
                min_index = j

        if min_index != i:
            alist[i],alist[min_index] = alist[min_index],alist[i]





alist = [54,226,93,17,77,31,44,55,20]

selection_srot(alist)

print(alist)

