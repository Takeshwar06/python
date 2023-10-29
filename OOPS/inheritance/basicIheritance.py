# Inheritance allows us to define a class that inherits all the methods and properties from another class.

# Parent class is the class being inherited from, also called base class.

# Child class is the class that inherits from another class, also called derived class.


class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")
x.printname()

# To create a class that inherits the functionality from another class, send the parent class as a parameter when creating the child class:

class Student(Person):
# Note: Use the pass keyword when you do not want to add any other properties or methods to the class.
  pass
x = Student("Mike", "Olsen")
x.printname()


# when we add __init__() function in child class then not called __inti__() function of parent class when we call child class
# Note: The child's __init__() function overrides the inheritance of the parent's __init__() function.