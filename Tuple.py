t1=("python",10,1.5,True,[1,2,3,],(10,20))
l1=["python",10,1.5,True,[1,2,3,],(10,20)]
print(len(t1))
#Accessing items of a tuple - index
print(t1[2])
print(t1[-2])
#Slicing in tuple
print(t1[2:4:1])
#Identifiy Data type
print(type(t1))
print(type(l1))
#can convert list into tuple
t2=tuple(l1)
print(t2,type(t2))