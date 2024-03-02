def strr(stroka):
    capital = 0
    lower = 0
    for x in stroka:
        if x >= 'A' and x <= 'Z':
            capital += 1
        if x >= 'a' and x <= 'z':
            lower += 1
    print(capital, lower)

stroka = input()
strr(stroka)