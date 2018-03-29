#encoding=utf-8

import re

ret = re.match("\w*","HHAHawaswHAHHAHaaaaaakkkkkk")
if ret != None:
    print(ret.group())



ret = re.match("[a-zA-Z0-9_]{6,100}","wdwdwdwadw121213131313")
if ret != None:
    print(ret.group())


ret = re.match("[a-zA-Z_]+[\w]*","naennennen_2_wdwa")
if ret != None:
    print(ret.group())



ret = re.match("[1-9]?[0-9]","120")
if ret != None:
    print(ret.group())


ret = re.match("[\w]{4,20}@163\.com$","wudezhi@163.com")
if ret != None:
    print(ret.group())


ret = re.match("\w{4,20}@(163|126|qq)\.com","494712390@qq.com")
if ret != None:
    print(ret.group())

ret = re.match("<[a-zA-Z]*>\w*<[a-zA-Z]*>","<html>hahhah<html>")
if ret != None:
    print(ret.group())


ret = re.findall(r"\d+","python = 9999, c = 7890, c++ = 12345")
if ret != None:
    print(ret)
    print(ret[0])


ret = re.sub(r"\d+","mySico","python === 123")
if ret != None:
    print(ret)


s = "<div>" \
    "  <p>岗位职责：</p>" \
    "<p>完成推荐算法、数据统计、接口、后台等服务器端相关工作</p>" \
    "<p><br></p>" \
    "<p>必备要求：</p>" \
    "<p>良好的自我驱动力和职业素养，工作积极主动、结果导向</p>" \
    "<p>&nbsp;<br></p>" \
    "<p>技术要求：</p>" \
    "<p>1、一年以上 Python 开发经验，掌握面向对象分析和设计，了解设计模式</p>" \
    "<p>2、掌握HTTP协议，熟悉MVC、MVVM等概念以及相关WEB开发框架</p>" \
    "<p>3、掌握关系数据库开发设计，掌握 SQL，熟练使用 MySQL/PostgreSQL 中的一种<br></p>" \
    "<p>4、掌握NoSQL、MQ，熟练使用对应技术解决方案</p>" \
    "<p>5、熟悉 Javascript/CSS/HTML5，JQuery、React、Vue.js</p>" \
    "<p>&nbsp;<br></p>" \
    "<p>加分项：</p>" \
    "<p>大数据，数理统计，机器学习，sklearn，高性能，大并发。</p>" \
    "</div>"


print("s === %s"%s)

print("===================\n")

ret = re.sub("</?\w>","",s)
print(ret )


ret = re.split(r":| ","info:dezhi 27 hubei")
if ret != None:
    print(ret)
    