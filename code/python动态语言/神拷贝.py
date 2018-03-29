#encoding=utf-8
import copy

c = [1,3,5,7,9]



print(id(c))
print(c)

b = copy.deepcopy(c)

print(id(b))
print(b)



c.append(23)

print(c)
print(b)