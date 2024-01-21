#example 1

print(10 > 9) #true
print(10 == 9) #false
print(10 < 9) #false

#example 2

a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

#example 3
  
print(bool("Hello")) #true because str is not empty
print(bool(15)) #true because int > 0

#example 4

x = "Hello"
y = 15

print(bool(x))
print(bool(y))

#example 5

"""Almost any value is evaluated to True if it has some sort of content.

Any string is True, except empty strings.

Any number is True, except 0.

Any list, tuple, set, and dictionary are True, except empty ones."""

bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])

#example 6

#They are false
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})

#example 7

class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj)) #False, if not to use bool() there will be an adress of variable

#example 8

def myFunction() :
  return True

print(myFunction())

#example 9

def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")

#example 10
  
x = 200
print(isinstance(x, int)) #true because 200 is int





