# # a variable is a container that stores a value
# # called a variable as it can store different types of values
#
# num = 1
# dec = 3.5
# food = "chocolate"
#
# # == checks if values of 2 variables are the same
#
# print(f"num is a {type(num)} variable and value contained is: {num}")
# print(f"dec is a {type(dec)} variable and value contained is: {dec}")
# print(f"food is a {type(food)} variable and value contained is: {food}")
#
# # python being a strong typed means it enforces type rules, you cannot mix data types in one print function
# # being dynamically typed means that the variables are checked at run time for their type not when written
#
# num = 3
# print(num)
#
# # the value stored in the variable num now updates as it was assigned a new value
#
# x = 10
# y = x
# x = 13
#
# print(f"x is {x} & y is {y}")
#
# # value stored in x is 10 and y is given what x is
# # no because the value of x is changed after
#
# name = input("enter your name: ")
# age = input("enter your age: ")
# DOB = input("enter your DOB (dd/mm/yy): ")
# print(f"Hi your name is, {name}, you are {age} years old and your DOB is: {DOB}")

# consolidation task

name = input("enter your name: ")
age = int(input("enter your age: "))
month = input("what month were you born? ")
year = input("what year were you born?")
print(f"Hi {name}, {age}\nyou were born in {month} of the year {year}")