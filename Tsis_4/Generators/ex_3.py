def gen(n):
    a = (x for x in range(n + 1))
    for x in a:
        if x % 3 == 0 and x % 4 == 0:
            print(x , end = " ")

n = int(input())
gen(n)