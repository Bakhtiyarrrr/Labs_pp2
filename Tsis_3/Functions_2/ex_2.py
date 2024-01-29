from data import *

def score_to_newlist(movie_s):
    m = False
    sublist = []
    for x in movie_s:
       for key, value in x.items():
          if key == "imdb" and value > 5.5:
            m = True
          if key == "imdb" and value < 5.5:
             m = False
       if m == True:
          sublist.append(x)
              
    return sublist
   

print(score_to_newlist(movies))