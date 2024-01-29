def histogram(numbers):
    for x in numbers:
        i = 0
        while i < x:
            print('*', end = '')
            i += 1
        print()

numbers = [int(x) for x in input().split()]
histogram(numbers)