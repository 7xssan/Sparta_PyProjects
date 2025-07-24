# Script should act like a waiter at a restaurant taking orders
# level 1
# Greet the user
# Print a list of starters
# Take an input for the user for their starter
# Print a list of mains
# Take an input for the user for their main course
# Print a list of desserts
# Take an input for the user for their dessert
# Print all of the user's choices

starters = {
    "falafel": 5.99,
    "houmus": 3.50,
    "soup": 3.50,
    "cheese sticks": 4.99}

mains = {
    "mandhi": 14.99,
    "maqluba": 15.99,
    "mansaf": 16.99,
    "shawarma": 9.99}
desserts = {
    "qata'if": 7.99,
    "knafeh": 8.99}
customer_order_list = {}
bill = 0
starter_quantity = 0
main_quantity = 0
dessert_quantity = 0

print("Hi, welcome to the xyz restaurant!")

print(starters)
starter = input("what would you like for your starter?: ")
if starter in starters:
    starter_quantity += int(input(f"How many {starter} portions would you like?: "))
    customer_order_list.append(starter)
    bill += starters[starter] * starter_quantity
else:
    print("That is not in the menu!")

print(mains)

main = input("what would you like for your main?: ")
if main in mains:
    main_quantity += int(input(f"How many {main} portions would you like?: "))
    customer_order_list.append(main)
    bill += mains[main] * main_quantity
else:
    print("That is not in the menu!")

print(desserts)
dessert = input("what would you like for your dessert?: ")
if dessert in desserts:
    dessert_quantity += int(input(f"How many {dessert} portions would you like?: "))
    customer_order_list.append(dessert)
    bill += desserts[dessert] * dessert_quantity
else:
    print("That is not in the menu!")

print(f"alright so your order is {starter} for your starter, {main} for your main and {dessert} for your dessert")
print(f"the total for your order is £{bill:.2f}. ")
print(customer_order_list)