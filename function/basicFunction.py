# A function is a block of code which only runs when it is called.

# You can pass data, known as parameters, into a function.

# A function can return data as a result.

# pass keyword in function
def myfunction(): # simply ignore 
  pass

def my_function():
  print("my_function is called")


my_function()


# function with argument
def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")