list_data = [1, 2, 3, 4, 5]
embedded_lists = [[1,2,3],[4,5,6]]
dict_data = {1: {"name": "Bronson", "money": "$0.05"}, 2: {"name": "Masha", "money": "$3.66"}, 3: {"name": "Roscoe", "money": "$1.14"}}

for num in list_data:
    print(num * 2)

for data in embedded_lists:
    print(data)
    for values in data:
        print(values)


for d_value in dict_data.values():
    for key_val in d_value.values():
        print(key_val)

for d_value in dict_data.values():
    print(d_value ["money"])