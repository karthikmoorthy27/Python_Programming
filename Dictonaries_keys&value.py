from sys import stdin

student1 = {'id':1001,'name':"john",'marks':[89.5,71.5,81.0]}
print(student1)
print(student1['marks'])
print(student1['marks'][1])
student2 = {'id':1001,'name':"john",'marks':{'eng':89.5,'maths':71.5,'bio':81.0}}
print(student2['marks']['eng'])
#fetch the keys"

print(student1.keys())
#fetch the value"
print(student1.values())
#fetch items
print(student1.items())


