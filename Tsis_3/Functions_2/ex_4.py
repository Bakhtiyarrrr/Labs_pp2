from data import *
def average(some_list):
    average_1 = 0
    for x in some_list:
        for key, value in x.items():
            if key == "imdb":
                average_1 += float(value)
    
    return average_1 / len(some_list)


print(average(movies))