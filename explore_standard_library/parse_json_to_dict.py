import json

with open('servers.json', 'r') as read_file: # opening json file as 'r' which opens an existing file to read from, used to load or view data
    servers = json.load(read_file) # load function converts argument passed from json back to python
    print(servers)
    print(type(servers))
    print(servers["server1"])
    print(servers["server2"])

    for server_keys, server_values in servers.items():
        print(f"key and value: '{server_keys} = {server_values}'")
        for sub_key, sub_values in server_values.items():
            print(f"sub keys and sub values: '{sub_key} = {sub_values}'")
