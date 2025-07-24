# sets are unordered, unlike lists and tuples which can allow items accessed by index number
# sets remove duplicates automatically

fruits = {"apple", "banana", "cherry"}
print(fruits)
fruits.add("orange")
print(fruits)
# fruits.remove("banana")
print(fruits)
fruits.add("apple")
print(fruits)
print(type(fruits))