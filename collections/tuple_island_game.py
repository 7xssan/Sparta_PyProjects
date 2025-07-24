# tuples and lists can both store data of various types
# tuples are immutable meaning they cannot be edited or changed after made
# data types such as string, int, bool etc are immutable as they are given a specific value
# use cases for tuples can be a list of coordinates, list of instructions
# the following code creates a tuple called essentials with 2 items and prints, then counts how many times "bread" is in the tuple

# "Stranded on a Desert Island" game
# Rationale: Practice tuples
# Type of exercise: Finish the code
print("You are stranded on a desert island. You can take only THREE items.")
essential_item1 = input("What is an essential item you would take? ")
essential_item2 = input("What is an essential item you would take? ")
essential_item3 = input("What is an essential item you would take? ")
# save the items as a tuple
essentials_tuple = (essential_item1, essential_item2, essential_item3)
# print the tuple
print("Here are your items as a tuple:", essentials_tuple)
print("")
print("I lied. You can take one more item.")
essential_item4 = input("What is one more essential item you would take? ")
# try to add the 4th item to the tuple
# if you can't add the 4th item, work out how to save the 4th item to the tuple
essentials_tuple = essentials_tuple + (essential_item4,)

print("Here are your items as a tuple (with the 4th item added):", essentials_tuple)