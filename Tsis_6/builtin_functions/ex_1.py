
def mult(numbers):
   t = 1
   for x in numbers:
      t = x * t
   print(t)



numbers = [int(value) for value in input().split()]
mult(numbers)
