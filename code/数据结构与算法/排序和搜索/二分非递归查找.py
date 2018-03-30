#coding=utf-8

def binary_search(alsit,item):

    first = 0

    last = len(alsit)-1

    while first <= last:

        midPoint = int((first + last)/2)

        if alsit[midPoint] == item:
            return True

        elif alsit[midPoint] < item:
            first = midPoint + 1
        else:
            last = midPoint - 1
    return  False



testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42]

isOK = binary_search(testlist,17)


print(binary_search(testlist,17))

# print(binary_search(testlist, 3))
# print(binary_search(testlist, 13))


