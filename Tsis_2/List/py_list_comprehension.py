#example 1

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

#example 2 /analog example 1

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)

#example 3

newlist = [x for x in fruits if x != "apple"]

#example 4

newlist = [x for x in range(10)]

#example 5

newlist = [x for x in range(10) if x < 5]

#example 6

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x.upper() for x in fruits]

print(newlist)

#example 7

newlist = ['hello' for x in fruits]

#example 8

newlist = [x if x != "banana" else "orange" for x in fruits]


