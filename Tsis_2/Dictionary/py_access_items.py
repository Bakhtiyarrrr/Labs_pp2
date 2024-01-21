#example 1

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]

#example 2

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]

#example 3

x = thisdict.get("model") #return Mustang

#example 4
#The keys() method will return a list of all the keys in the dictionary.
x = thisdict.keys() 

#example 5

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.keys()

print(x) #before the change

car["color"] = "white"

print(x) #after the change

#example 6
#return the list of values of dictionary
x = thisdict.values()

#example 7

#The items() method will return each item in a dictionary, as tuples in a list.
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = thisdict.items()

print(x) #dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964)])

#example 8

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")
  

