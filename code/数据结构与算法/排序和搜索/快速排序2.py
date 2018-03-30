#coding=utf-8

def quick_sort(alist,start,end):

    if start >=end:
        return

    mid = alist[start]

    low = start

    heigh = end



    while low < heigh:

        while low < heigh and alist[heigh] >= mid:
            heigh -= 1

        alist[low] = alist[heigh]


        while low < heigh and alist[heigh] < mid:
            low += 1

        alist[heigh] = alist[low]


    alist[low] = mid

    quick_sort(alist,start,low-1)
    quick_sort(alist,low+1,end)



alist = [54,26,93,17,77,31,44,55,20]
quick_sort(alist,0,len(alist)-1)
print(alist)
