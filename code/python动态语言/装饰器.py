#coding=utf-8

def w1(func):
    def inner():
        print("====W1======")
        func()
        print("++++++++")

    return inner






@w1
def f1():
    print("00000000000000")
    print(id(f1))
    print("f1")


print("9999999999999")
print(id(f1))

f1()