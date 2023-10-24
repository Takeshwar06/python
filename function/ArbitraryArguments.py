def my_function(*kids): #*kids is tuple
  print(kids) # ("tiger","Tobias","Linus")

my_function("tiger", "Tobias", "Linus")


def my_function(tiger,*kids): #*kids is tuple
  print(tiger,kids) # tiger ("tobias",)

my_function("tiger", "Tobias", "Linus")