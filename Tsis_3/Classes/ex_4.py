class Point:
   def __init__(self, x, y, u, t):
      self.x = x
      self.y = y
      self.u = u
      self.t = t

   def show_first(self):
      print(self.x, self.y)

   def show_second(self):
      print(self.u, self.t)

   def move_first(self):
      z = self.x
      self.x = self.y
      self.y = z
   def move_second(self):
      c = self.u
      self.u = self.t
      self.t = c
   def dist(self):
      print(((self.x - self.u)**2 + (self.y - self.t)**2)**0.5) 


cordinates = Point(2,4,5,6)
cordinates.move_first()
cordinates.show_first()
cordinates.dist()

