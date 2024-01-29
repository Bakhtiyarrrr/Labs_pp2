from ex_2 import *

class Rectangle:
    def __init__(self, length):
        self.len = length
        self.width = int(input())
    def area_of_rectangle(self):
        print(self.len * self.width)



example = Shape.Square(input())
rectangle = Rectangle(example.length)
rectangle.area_of_rectangle()

