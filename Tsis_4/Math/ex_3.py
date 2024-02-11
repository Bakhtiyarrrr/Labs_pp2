import math
number_of_sides = 4
length_of_side = 25
R = (length_of_side)/(2 * math.sin(math.radians(180/number_of_sides)))
print(round(0.5 * R**2 * number_of_sides * math.sin(math.radians(360/number_of_sides))))
