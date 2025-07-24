import json

with open('servers.json', 'r') as read_file:
    # servers = json.loads(read_file) loads function expects raw string that has json. not a file
    # the content of the file is being read as a string and stored
    json_str = read_file.read()

    # loads function converts only json string not the file back into a python dictionary
    servers = json.loads(json_str)

    print(servers)
    print(type(servers))
    print(servers["server1"])
    print(servers["server2"])

    for server_keys, server_values in servers.items():
        print(f"key and value: '{server_keys} = {server_values}'")
        for sub_key, sub_values in server_values.items():
            print(f"sub keys and sub values: '{sub_key} = {sub_values}'")