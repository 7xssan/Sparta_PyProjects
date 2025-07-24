import json
import os
import sys
import yaml

# Checking there is a file name passed
if len(sys.argv) > 1:
    # Opening the file
    if os.path.exists(sys.argv[1]):
        source_file = open(sys.argv[1], "r") # file will be opened as read to load data
        source_content = json.load(source_file) # data passed as argument will be converted to python from json
        source_file.close() # the opened file is now closed
        output_yaml = yaml.dump(source_content) # converts python dict into yaml string
        print(type(output_yaml))
        if len(sys.argv) > 2:  # checking if second argument was passed, this will be the new file to save converted data
            target_file = sys.argv[2]
        else:  # if a filename was not given then yaml will be printed to the screen
            print("YAML output:")
            print(output_yaml)

        # 2.2 Check the target file doesn't already exist
        if os.path.exists(target_file):  # this line checks if argument passed in method actually exists
            print("the target file already exists")

        # 2.3 If previous conditions not met, then save YAML file
        else:
            with open(target_file, 'w') as yaml_file:  # file being created/opened as object
                yaml_file.write(output_yaml)  # yaml output is being written in new file
                print(
                    f"yaml output was successfully written to {target_file}")  # printing success message and showing file name as place its saved in
        # Failing if the file isn't found
    else:
        print("ERROR: " + sys.argv[1] + " not found")
        exit(1)
    # No source file specified
else:
    print("ERROR: No JSON file was specified")
    print("Usage: json2yaml.py <source_file.json> <target_file.yaml>")

# 1. Convert the JSON to YAML - use yaml library

 # converts the python into yaml

# 2. Save the YAML into a new file with the name for it received as a argument
# 2.1 Check the target file name was specified as an argument, if not, output the YAML to the screen instead
