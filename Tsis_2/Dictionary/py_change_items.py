#example 1

#Change 1964 to 2018
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2018

#example 2
#Add new pair
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
car.update({"size":100})
print(car)
# {"brand": "Ford", "model" : "Mustang", "year": 1964, "size": 100}


