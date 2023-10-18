# take multiple values or inputs in one line by two methods. 

# Using split() method --> This function helps in getting multiple inputs from users. It breaks the given input by the specified separator. If a separator is not provided then any white space is a separator.

# Python program showing how to
# multiple input using split
 
# taking two inputs at a time
seprator="," #by default white space
x, y,z = input("by split() Enter two values: ").split() 

print("Number of boys: ", x)
print("Number of girls: ", y)
print("Number of total: ", z)


# Using List comprehension



# Python program showing
# how to take multiple input
# using List comprehension
 
# taking two input at a time
x, y = [int(x) for x in input("Enter two values: ").split()]
print("First number is {} and second number is {}".format(x, y))

# {} --> you can suppose like farmat specifire (%d,%c,%s,%f)
