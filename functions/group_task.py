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

def print_something_2(greeting):
    print(f"your greeting is: {greeting}")

print_something_2("good morning team!")

# 3 Make a more interesting version of a function that accepts one argument
# a. here is the code to call the function:
#    greet("Susan")
# b. You need to write the function
# c. Make sure the print statement in your function uses concatentation (ie. +) rather than an f-string
# d. Output should be: Hello, my name is Susan

def greet(name):
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