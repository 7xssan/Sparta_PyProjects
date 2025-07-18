import time
from datetime import datetime

name_str = input("enter your name: ")
age_int = int(input("enter your age: "))

current_year = 2025
year = current_year - age_int

print(f"OMG {name_str}, you are {age_int} years old so you were born in {year}")

birth_year = int(input("enter year of birth: "))

total_days = (current_year - birth_year) * 365
total_hours = total_days * 24

print(f"you have lived {total_hours} hours")

# get DOB details typcasted as string and store in appropriate named variables
birth_year = int(input("enter year of birth: "))
birth_month = int(input("enter month of birth (1-12): "))
birth_day = int(input("enter day of birth (1-31): "))

# make birth date variable, use datetime() function and pass inputted variables. make current time variable using date.now() function
birth_date = datetime(birth_year, birth_month, birth_day)
print(type(birth_date))
current_time = datetime.now()
print(type(current_time))
# make variable to store difference between current time and birth date. then make variable to store it as hours by /
time_difference = current_time - birth_date
hours_lived = time_difference.total_seconds() / 3600

print(f"you have lived for a total of {int(hours_lived)} hours!")

#
birthday_this_year = datetime(current_year, birth_month, birth_day)
days_till_bday = (birthday_this_year -  current_time).days

if current_time > birthday_this_year:
    print("your birthday has happened this year already!")
else:
    print(f"your birthday has not happened this year you have {days_till_bday} days left until your birthday")