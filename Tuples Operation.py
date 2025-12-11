"""
concatenation, repetition,membership,
count,index,
min,max,sum
"""
student_detail1=(1001,"John")
student_detail2=(78.5,91.0,83.5,79.5)

#+ operator
student_details=student_detail1+student_detail2
#print(student_details)
#* Operator
t1=("class5", 5000)
#print(t1*3)
#Membership operator
#print(91.2 in student_details)
#count
t2=(10,4,1,9,0,3,1)
#print(t2.count(1))
#index
print(t2.index(1))# what is the index of 4 in tuple
#print(t2.index(42))#
#min()
print(f"Smallest Number : {min(t2)}")
print(f"Biggest Number : {max(t2)}")
print(f" Total : {sum(t2)}")

