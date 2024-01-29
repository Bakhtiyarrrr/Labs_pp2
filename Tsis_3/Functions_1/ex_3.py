def solve(num_heads,num_legs):
   for x in range(35):
      for y in range(35):
         if x + y == 35 and 2*x + 4*y == 94:
            print(x, y)
   return 0
num_heads = 35
num_legs = 94

solve(num_heads, num_legs)

