#coding=utf-8

def test1():
    print("-------in test1 func -----")


test1()


ret = test1

print(id(ret))

print(id(test1))


ret()