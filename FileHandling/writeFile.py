#Python writing files (.txt, .json, .csv)
#w- if file doesn't exist, it creates ; overwrites the content of the file
    #(any existing data will be removed)
#x - only writes if there is no file Use this mode when you want to ensure
    #that you don’t accidentally overwrite an existing file
#a - append the data Use this mode when you want to add data
#     to an existing file without erasing its content.

import json
import csv

employees_csv =  [["Name", "Age", "Job"],
             ["Spongebob", 30, "Cook"],
             ["Patrick", 37, "Unemployed"],
             ["Sandy", 27, "Scientist"]]

employee_json =  {
   "name": "Spongebob",
   "age": 30,
   "job": "Cook"
}

employees = ["Fatma", "Nikita", "Anusha", "Abhinash", "Sangam"]

txt_data = "I Like Pizza!"


file_path = "employee.csv"
try:
    with open(file_path, "w", newline="") as file:
        writer = csv.writer(file)
        for row in employees_csv:
            writer.writerow(row)

        # file.write(f"Change bayo hai kta ho.")
        # json.dump(employee_json, file, indent=4)

        print(f"csv file '{file_path} was created'")
except FileExistsError:
    print("That file already exists")
