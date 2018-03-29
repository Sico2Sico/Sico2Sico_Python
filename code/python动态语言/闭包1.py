#coding=utf-8

# def counter(start=0):
#     def incr():
#         nonlocal start
#         start += 1
#         return start
#     return incr
#
# c1 = counter(5)
# print(c1())
# print(c1())


def line_conf(a,b):
    def line(x):
        return a*x + b
    return line


line1 = line_conf(1,1)
print(line1(2))
