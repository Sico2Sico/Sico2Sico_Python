#coding=utf-8

import re

result = re.match("itcast","itcast.com")

print(result)

if result != None:
    tmpStr = result.group()
    print(tmpStr)

ret = re.match("h","hello word")
if ret != None:
    tmps = ret.group()
    print(tmps)

print("==============================")
ret = re.match("H","Hello word")
if ret != None:
    tmps = ret.group()
    print(tmps)



print("==============================")
ret = re.match("[hH]","Hello hword")
if ret != None:
    tmps = ret.group()
    print(tmps)

ret = re.match("[hH]","hello Hword")
if ret != None:
    tmps = ret.group()
    print(tmps)


print("=====end====")
ret = re.match("\d","1Hello 3hword5")
if ret != None:
    tmps = ret.group()
    print(tmps)