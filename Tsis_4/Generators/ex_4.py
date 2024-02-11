x, y = map(int, input().split())
a = (h ** 2 for h in range(x, y + 1))
for f in a:
    print(f, end = " ")