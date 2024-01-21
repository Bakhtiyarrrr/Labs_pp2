#example 1

thistuple = ("apple", "banana", "cherry")
print(thistuple)

"""
Tuple Items
Tuple items are ordered, unchangeable, and allow duplicate values.

Tuple items are indexed, the first item has index [0], the second item has index [1] etc.

Ordered
When we say that tuples are ordered, it means that the items have a defined order, and that order will not change.

Unchangeable
Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.

Allow Duplicates
Since tuples are indexed, they can have items with the same value:
"""
#example 2

thistuple = ("apple", "banana", "cherry")
print(len(thistuple))

#example 3

thistuple = ("apple",)
print(type(thistuple))
#NOT a tuple
thistuple = ("apple")
print(type(thistuple))

#example 4

mytuple = ("apple", "banana", "cherry")
print(type(mytuple))




