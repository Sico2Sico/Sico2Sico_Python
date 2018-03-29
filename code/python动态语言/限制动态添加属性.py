#coding=utf-8

class Person(object):
    __slots__ = ("name","age")


p = Person()
p.name = "德志"
p.age = 27

print(p)