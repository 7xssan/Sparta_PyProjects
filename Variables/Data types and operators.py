# operator is the specific action being used on the operand/s

# x = 5
# y = 1
#
# print(x + y)
# print(x - y)
# print(x * y)
# print(x / y)
# print(x % y)
# print(x > y)
# print(x < y)
# print(x == y)
# print(x != y)
# print(x >= y)
# print(x <= y)

# the string fails because it has double quotes at the end, closed the first and the extra opened another
# if your string contains quotes, use single quotes and vice versa

# string slicing lets you get specific characters in string by using indexed numbers

Hw = "Hello world!"

print(Hw)

print(len(Hw))
print(Hw[0])
print(Hw[-1])
print(Hw[-2])

# This starts the print string from the 3rd character to the end

print(Hw[2:])

# This starts the string from the 3rd last character to the end

print(Hw[-3:])

# this starts the string from the first character to the fifth

print(Hw[:5])

# Starts from the second, stops at the fifth (doesn't include it)

print(Hw[1:4])

