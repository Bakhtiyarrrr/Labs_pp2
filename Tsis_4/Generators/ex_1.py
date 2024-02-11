n = int(input())
a = (x ** 2 for x in range(n))
for x in a:
    print(x, end = " ")
