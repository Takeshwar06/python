# Note: The self parameter is a reference to the current instance of the class, and is used to access variables that belong to the class.

#self is like this key reference ot current object
class student:
    name="tiger"
    age=21
    subject="math"
    #method
    def getInfo(self):
        print(self.name,self.age)

a=student()
print(a.name,a.age)

#set info of student
b=student()
b.name="amit"
b.age=17
b.getInfo() # print self.name and self.age 
