from random import choice


def add(int1, int2):
    return int1 + int2

def subtract(int1, int2):
    return int1 - int2

def multiply(int1, int2):
    return int1 * int2

def divide(int1, int2):
    if int2 == 0:
        return "Error: you cannot divide by 0!"
    return int1 / int2

def exponentiate(int1, int2):
    return int ** int2


print("welcome to simple calculator!")
print("1. add")
print("2. subtract")
print("3. multiply")
print("4. divide")
print("5. exponentiate")
print("6. ...")

choice = input("what option would you like to choose (1-6): ")

if choice in ['1', '2', '3', '4', '5']:
    value1 = float(input("enter number: "))
    value2 = float(input("enter number: "))

    if choice == '1':
        result = add(value1, value2)
        print(f"{value1} + {value2} = {result}")
    elif choice == '2':
        result = subtract(value1, value2)
        print(f"{value1} - {value2} = {result}")
    elif choice == '3':
        result = multiply(value1, value2)
        print(f"{value1} x {value2} = {result}")
    elif choice == '4':
        result = divide(value1, value2)
        print(f"{value1} / {value2} = {result}")
    elif choice == '5':
        result = exponentiate(value1, value2)
        print(f"{value1} ** {value2} = {result}")

elif choice == '6':
    print("...")
else:
    print("choice invalid. please select a number shown!")