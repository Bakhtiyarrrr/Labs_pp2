from data import *
def categoory(name_of_category):
    for x in movies:
        for key,value in x.items():
            if key == "name":
                name = value
            if key == "category" and value == name_of_category:
                print(name)
    
name_of_categore = input()
categoory(name_of_categore)
