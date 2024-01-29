import math
def volume(r):
    n = 4/3
    print(n * math.pi * (r**3))


def histogram(numbers):
    for x in numbers:
        i = 0
        while i < x:
            print('*', end = '')
            i += 1
        print()

def palindrome(stroka):
    stroka2 = list(reversed(stroka))
    stroka2 = "".join(stroka2)
    if stroka == stroka2:
        print("Yes, it is palindrome!")
    else:
        print("No, it is not palindrome!")    

def spy_game(numbers):
    m = False
    stroka = ''
    for i in range(len(numbers)):
        stroka += str(numbers[i])
    if '007' in stroka:
      m = True
    return m


def has_33(numbers):
    m = False
    for i in range(len(numbers)):
        if i == len(numbers) - 1:
            break
        if numbers[i] == 3 and numbers[i+1] == 3:
            m = True
            break
    return m  