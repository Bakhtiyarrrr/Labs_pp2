from data import *

def tiki(categoryy):
    counter = 0
    average_2 = 0
    for x in movies:
        average_1 = 0
        for key, value in x.items():
            if key == "imdb":
                average_1 = value
            if key == "category" and value == categoryy:
                average_2 += average_1
                counter += 1

    return average_2 / counter

stroka = input()
print(tiki(stroka))
