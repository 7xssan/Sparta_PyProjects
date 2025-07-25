# 1 Make a function with no argument
# Name it 'print_something' and all it should do it print something to the screen
# Call the function to test it works

def print_something():
    print("hello world!")

print_something() # calls function

# 2 Make a function with one argument

# A. Aim: Improve the last function by having it receive an argument to replace the 'hard coded' string
# B. Make a new improved function which
#       I.  Accepts a string variable as an argument
#       II. Prints the string variable received as an argument

def print_something_2(greeting: str):
    print(f"your greeting is: {greeting}")

print_something_2("good morning team!")

# 3 Make a more interesting version of a function that accepts one argument
# a. here is the code to call the function:
#    greet("Susan")
# b. You need to write the function
# c. Make sure the print statement in your function uses concatentation (ie. +) rather than an f-string
# d. Output should be: Hello, my name is Susan

def greet(name: str):
    print("hello, my name is " + name + ".")

greet("Susan")

# 4. Make a function with 2 arguments that returns a value
# a. Troubleshoot this code so that the function returns the correct value of 4:def addition(int1, int2):
#     int1 + int2
# print(addition(2, 2))
# b. This time we do NOT want the function to do the print to the screen
# c. Document what you've learnt

#  the defined function addition accepts 2 arguements, it returns an addition of the arguements
def addition(int1, int2):
    return int1 + int2
# sum is declared variable that calls function and passes 2 as arguments and stores the result. is then printed to screen
sum = addition(2, 2)
print(sum)

# 5. Make a function with default values
# a. Copy your working code from the last exercise (that adds 2 and 2 together) as starting code for this exercise
# b. Replace line of code to call the function with this:
#    print(addition())
# c. Run your code - you should get an error
# d. Modify your function so that int1 and int2 both have the default value of 2
# e. Run your code and make sure the result is 4
# f. Now call your function with this line of code:
#    print(addition(4, 4))
# g. Explain why the answer is now 8

def addition(int1=2, int2=2):
    return int1 + int2

# these passed arguments will override the default values set
print(addition(4,4))

# 6. Make a function that accepts any number of arguments
# a. Design a function called 'print_every_number' which accepts a tuple of numbers as an argument
# b. The function should do 2 things:
#       Print the type of the tuple that was passed in as an arguments
#       Loop through the tuple and print each item in the tuple on a separate line
#
# c. After calling the function, the output should be:
# <class 'tuple'>
# 1
# 2
# 2
# 3
# 3
# 4
# 5
# 5
# d. Explain what character allows your function to accept multiple arguments

def print_every_number(*numbers):
    print(type(numbers))
    for num in numbers:
        print(num)


print_every_number(1, 2, 2, 3, 3, 4, 5, 5)

# 7.Make a function which gives a hint about an argument's data type
# Some people think stricter typing should be used with Python as best practice, let's find out why
# See what happens if you call your earlier greet function with this line of code:
# greeting(24601)
#
# To HELP us avoid this type of error, define the type of argument accepted into our function so that we are given a warning BEFORE we even run out Python script:
# Define that data type accepted by your greet function ids a string
# Notice that PyCharm now gives the warning Expected type 'str', got 'int' instead BEFORE you even run your code

# 8.Make a function which gives a hint about a return value's data type
#
# Let's make a new function to bring it all together, also to provide type hints for all arguments, function return values and variables used...
#
# a. The function should be named division:
#
# i. It should divide 2 integers accepted as arguments
#
# ii. It should return the result of the division
#
# iii. The arguments should:
#       have their types defined
#       have the default values of 2 and 5 (therefore, by default 2 will be divided by 5 and have the result 0.4)
# 1v. NEW! Define the value returned as a float for the type hint
# b. NEW! Before calling the function, define variables a and b in Python as statically-defined integers with the values 4 and 6
# c. You should call the function with this line of code:print(division(a, b))
# d. Also check the default values work if no values are passed into the function

def divide(int1: int = 2, int2: int = 5) -> float:
    if int2 == 0:
        return "Error: you cannot divide by 0!"
    sum = int1 / int2
    return sum

a: int = 4
b: int = 6
print(divide())

# 9. What are some good practices when it comes to functions?
# should have clear, descriptive name
# one focus, function has defined use
# type hints for self documentation
# always return something
