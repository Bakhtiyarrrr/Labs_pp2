def prime(numbers):
    x = lambda num: (num > 1) and all([num % i != 0  for i in range(2, int(num ** 0.5) + 1)])

    return [i for i in numbers if x(i) == True]


numbers = [int(value) for value in input().split()]
print(prime(numbers))