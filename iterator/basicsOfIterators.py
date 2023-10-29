# Lists, tuples, dictionaries, and sets are all iterable objects. They are iterable containers which you can get an iterator from.

# All these objects have a iter() method which is used to get an iterator:

# Return an iterator from a tuple, and print each value:

mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit)) # apple
print(next(myit)) # banana
print(next(myit)) # cherry

# iterator in string object
mystr = "banana"
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

# Iterate the values of a tuple:

mytuple = ("apple", "banana", "cherry")

for x in mytuple:
  print(x)