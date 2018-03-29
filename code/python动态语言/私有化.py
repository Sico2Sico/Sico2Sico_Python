#coding=utf-8

class Person(object):
    def __init__(self,name, age, taste):
        self.name = name
        self.age = age
        self.taste = taste


    def showperson(self):
        print(self.name)
        print(self.age)
        print(self.taste)



    def dowork(self):
        self._work()
        self.__away()

    def _work(self):
        print("my _work")

    def __away(self):
        print("my __away")




class Student(Person):
    def construction(self,name,age,taste):
        self.name = name
        self._age = age
        self.__taste = taste

    def showstudent(self):
        print(self.name)
        print(self.age)
        print(self.taste)


    @staticmethod
    def testbug():
        _Bug.showBug()


class _Bug(object):
    @staticmethod
    def showBug():
        print("showBug")


s1 = Student("德志",27, "Mac")
s1.showstudent()