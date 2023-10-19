# is --> It is used to test if two variables are equal

print("Demonstrate is key word")
a=5
b=7
c=a
print(a is b) # false
print(b is c) # false
print (a is c) #true
print(c is a)  #true

# in --> To check if a value is present in a Tuple, List, etc.

print("\n\nDemonstrate in key word")
list=[2,4,5,32,"tiger","amit"]
print("tiger" in list) # true
print("tigerjanghel" is list) # false

# you can apply is key word in string also
print("\nin key word in string")
name="Takeshwar"
print("kesh" in name) #true
print("fkfjf" in name) #flase