import json
data = {"name": "Bakhtiyar", "age": 19, "city": "Almaty"}
file = open("Labs_pp2/Tsis_6/dir_files/files/data.json", "w")
json.dump(data, file,indent = 4)