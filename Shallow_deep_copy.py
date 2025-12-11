import copy
l1 = [1,2.5,[10,20,30],'Python']

#shallow copy
l2 = copy.copy(l1)
print(l2)
print(id(l1))
print(id(l2))

