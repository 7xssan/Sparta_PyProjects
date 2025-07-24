# create the dictionary
import json

servers_dict = {
    "server1": {
        "hostname": "web-server-1",
        "ip_address": "192.168.1.1",
        "role": "web",
        "status": "active"
    },
    "server2": {
        "hostname": "db-server-1",
        "ip_address": "192.168.1.2",
        "role": "database",
        "status": "maintenance"
    }
}

# to convert the dict to a JSON string, you use the dumps function
json_string = json.dumps(servers_dict, indent=3)

print("JSON-formatted string: ")
print(json_string)

# when writing with to a file, you are taking data and saving it to a file on your computer
with open('servers.json', 'w') as json_file: # with open function opens or creates a file, first arg passed is name and 'w' opens in write mode which creates or overwrites a file, used when you want to save new data
    json.dump(servers_dict, json_file, indent=3) # saving as file allows it to be referred to as an object

with open('servers.json', 'r') as read_file: # opens file as object named read_file
    data_loaded = json.load(read_file) # json.load function converts json formatted text back into python
    print("Validated JSON from file")
    print(data_loaded) # prints the formatted text to check
