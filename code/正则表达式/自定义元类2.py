#-*- coding:utf-8 -*-
def uopperAttr(future_class_name, future_class_parents, future_class_attr):

    #遍历属性字典，把不是__开头的属性名字变为大写
    newAttr = {}
    for name,value in future_class_attr.items():
        if not name.startswith("__"):
            newAttr[name.upper()] = value

    #调用type来创建一个类
    return type(future_class_name, future_class_parents, newAttr)

class Foo(object):
    bar = 'bip'

print(hasattr(Foo))
print(hasattr(Foo))

f = Foo()
# print(f.BAR)
