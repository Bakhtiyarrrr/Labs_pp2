import itertools

def permut_string(stroka):
    stroka = itertools.permutations(stroka)
    for x in stroka:
        print(x)


stroka = input()
permut_string(stroka)
  