#coding=utf-8

import types

class Person(object):
    num = 0

    def __init__(self,name=None, age = None):
        self.name = name
        self.age = age

    def eat(self):
        print("eat food")




def run(self,speed):
    print(" %s在移动，速度是 %d km/m"%(self.name,speed))



@classmethod
def testClass(cls):
    cls.num = 100


@staticmethod
def testStatic():
    print("-------statit method")


P = Person("德志",27)
P.eat()


P.run = types.MethodType(run,P)
P.run(1000)

print(Person.num)

Person.testClass = testClass
Person.testClass()

Person.statrt = testStatic

Person.statrt()


