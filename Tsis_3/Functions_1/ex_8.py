def spy_game(numbers):
    m = False
    stroka = ''
    for i in range(len(numbers)):
        stroka += str(numbers[i])
    if '007' in stroka:
      m = True
    return m
numbers = [int(value) for value in input().split()]
print(spy_game(numbers))