# List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.

# normal technique
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist=[]

for item in fruits:
    newlist.append(item)

print(newlist)

languages=["cpp","java","python","javascript"]

newPrograming=[x for x in languages if "java" in x] # with condition
print(newPrograming)

# tiger=newPrograming #you can do also 
