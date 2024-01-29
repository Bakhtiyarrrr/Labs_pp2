
def prime(n):
  m = False
  i = 2
  while i <= int(n ** 0.5):
     if n % i == 0:
       m = True
       break
     i += 1
  return m
    

def filter_prime(numbers):
   for x in numbers:
       if prime(x) == False:
          print(x, end = " ")
   return 0
  
numbers = [int(value) for value in input().split()]  
filter_prime(numbers)
