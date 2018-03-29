#coding=utf-8

def makeBold(fn):
    def wrapped():
        return "<b>" + fn() + "</b>"
    return wrapped


def makeItalic(fn):
    def wrapped():
        return "<i>"+fn()+"<i>"
    return wrapped



@makeBold
def test1():
    return "hello world_1"


@makeItalic
def test2():
    return "hello Word_2"

@makeItalic
@makeBold
def test3():
    return "hello word_3"



print(test1())
print(test2())
print(test3())



