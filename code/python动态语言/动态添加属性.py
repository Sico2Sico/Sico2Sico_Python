#coding=utf-8


class Person(object):
    def __init__(self, name = None,age=None):
        self.name = name
        self.age = age


Person.sex = None

p = Person("德志",27)
print(p)
print(p.age)
print(p.name)
print(Person.sex)



