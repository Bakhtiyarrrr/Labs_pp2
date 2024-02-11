n = int(input())
a = (x for x in range(n + 1))
for x in a:
    if x % 2 == 0:
     print(x, end = ", ")

