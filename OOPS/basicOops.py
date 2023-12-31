# Python is an object oriented programming language.

# Almost everything in Python is an object, with its properties and methods.

# A Class is like an object constructor, or a "blueprint" for creating objects.

class Person:
  def __init__(self, name, age): # The __init__() function is called automatically every time the class is being used to create a new object.
    self.name = name
    self.age = age

  def __str__(self):#The __str__() function controls what should be returned when the class object is represented as a string.
    return f"{self.name}({self.age})"

p1 = Person("John", 36)

print(p1)