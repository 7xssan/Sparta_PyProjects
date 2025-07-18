# str_with_extra_spaces = "   extra spaces at the start and end   "
#
# the variable is put into the len function which checks the amount of characters in the string
#
# print(len(str_with_extra_spaces))
#
# the strip function removes any blank space in string variable and the len function returns the variable new length
#
# print(len(str_with_extra_spaces.strip()))
#
# example_text = "here's some text with some words of Text"
#
# this counts how many times the substring 'text' occurs within example_text & prints it to the screen
#
# count = example_text.count("text")
# print(count)
#
# converts example_text to lowercase & prints it to the screen
#
# print(example_text.lower())
#
# convert example_text to uppercase & print it to the screen
#
# print(example_text.upper())
#
# # capitalises the first letter in example_text & prints it to the screen
#
# print(example_text.capitalize())
#
# # replaces the word 'with' in example_text with a comma & prints it to the screen
#
# print(example_text.replace("with", ","))

# x = str(2)
#
# y = str(5.4)
#
# z = " there's now a number 25.4 unless we put a space in!"
#
# print(x + y + z)

# the problem is that the data types are different and python is a strong type language that enforces data types, so to fix that x and y variables were typecasted into string to make it run

# int_string = "6"
#
# convert int_string to an integer
#
# int_string = int(int_string)
# print(type(int_string))
# after converting, print its data type to the screen
#
# convert int_string to float
#
# int_string = float(int_string)
# print(type(int_string))
# after converting, print its data type to the screen

# name = "Lassie"
#
# years = 7
#
# height_cm = 60.2

# print these variables in an f-string so that it outputs this to the screen:

# "Lassie is 7 years old and 60.2 cm tall."

# print(f"{name} is {years} years old and {height_cm} cm tall")

# pi = 3.14159265359

# Use an f-string to print pi to 3 decimal places e.g. 'Pi to 3 decimal places: <value>'

# print(f"Pi to 3 decimal places: {pi:.3f}")

# Use an f-string to print pi to 5 decimal places e.g. 'Pi to 5 decimal places: <value>'

# print(f"Pi to 5 decimal places: {pi:.5f}")

score = 16

max_score = 26

score_as_decimal = score / max_score

# Use an f-string to print 'score_as_decimal' e.g. 'You scored 0.6153846153846154' (no % sign)

print(f"You scored {score_as_decimal}")

# Use an f-string to print 'score_as_decimal' formatted as a percentage e.g. 'You scored 61.538462%'

print(f"You scored {score_as_decimal:%}")

# Use an f-string to print 'score_as_decimal' formatted as a percentage to rounded to 2 decimal places e.g. 'You scored 61.54%'

print(f"You scored {score_as_decimal:.2%}")

# Use an f-string to print 'score_as_decimal' formatted as a percentage to rounded to a whole number e.g. 'You scored 62%'

print(f"You scored {score_as_decimal:.0%}")
