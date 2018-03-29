#coding=utf-8
import  sys

import hashlib

a = "hello word"
print(sys.getrefcount(a))




m = hashlib.md5()

md = m.update("wdawdwa")

print m.hexdigest()



