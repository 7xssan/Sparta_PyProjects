# shopping_list = ["eggs", "bread", "bananas", "biscuits", "milk"]
# print(shopping_list)
# print(type(shopping_list))
# print(shopping_list[0])
# print(shopping_list[-1])
#
# # use index method on shopping list bread to store index number
# index = shopping_list.index("bread")
# # change the value of the index in list to rice
# shopping_list[index] = "rice"
# print(shopping_list)
#
# shopping_list.append("carrots")
# print(shopping_list)
# print(len(shopping_list))
#
# another_list = ["toffee", "coffee"]

# __add__ method adds another list passed as argument to the object
# shopping_list = shopping_list.__add__(another_list)
# print(shopping_list)

# remove method removes what is passed as argument from the list
# print(shopping_list)
# shopping_list.remove("bananas")

# pop method removes last item in list
# shopping_list.pop()
# print(shopping_list)

# 1.Use your code from the "Task: Python variable basics" (last subtask) where you asked the user for their name, age and DOB.
# 2.Mix the name, age and DOB into one list user_details_list
# 3.Print the user's name, age and DOB from the list
# 4.Check the age is saved as an integer in the list. If it's not, work out how to convert it to an integer and add the age integer to the list.
# 5.Ask the user for their height in cm and save it to the variable height
# 6.Save height as a float in the list, and print the height from the list.

# name = input("enter your name: ")
# age = input("enter your age: ")
# DOB = input("enter your date of birth (dd/mm/yyyy):  ")
# height = input("enter your height (cm): ")
#
#
# user_details_list = [name, age, DOB]

# user_details_list.append(height)  adding new height variable into list

# user_details_list[-1] = float(user_details_list[-1])
# user_details_list[1] = int(user_details_list[1])
# print(type(user_details_list[1])) checks if index one variable is stored as integer
# print(type(user_details_list[-1]))
# print(user_details_list)

#Returns the 2nd and 3rd items in the list -> It should return [2, 3]
#Returns every second item in the list -> It should return [1, 3, 'two']
#Start at the last item, stop at the 3rd last item, and step in reverse order -> It should return ['three', 'two']

mixture = [1, 2, 3, "one", "two", "three"]

print(mixture[1:3])
print(mixture[::2])
print(mixture[-1:-3:-1])