
import json
import csv
file_path = "employee.csv"
try:
    with open(file_path, "r") as file:
        # content = file.read()
        # content = json.load(file)
        content = csv.reader(file)
        for line in content:
            print(line)
        print(content)
except FileNotFoundError:
    print("File not found!")
except PermissionError:
    print("You do not have permission to read that file!")


