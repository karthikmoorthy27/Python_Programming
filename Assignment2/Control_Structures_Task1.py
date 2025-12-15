"""
Task 1: Check if a Number is Even or Odd
"""
# Takes an integer input from the user.

num = int(input("Enter an number : "))

#Checks whether the number is even or odd using an if-else statement.

if num % 2 == 0:
    print(f"{num} is an even number")
else:
    print(f"{num} is an odd number")

