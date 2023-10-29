# Python also has a super() function that will make the child class inherit all the methods and properties from its parent:

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")
x.printname()

class Student(Person):
# Note: Use the pass keyword when you do not want to add any other properties or methods to the class.
  pass

class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)