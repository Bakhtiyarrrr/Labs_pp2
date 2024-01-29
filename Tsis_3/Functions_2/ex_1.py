from data import *
def score_above(mape:dict):
    m = False
    for key, value in mape.items():
        if key == "imdb" and value > 5.5:
            m = True
    return m        


for x in movies:
    truth = score_above(x)
    print(truth)


