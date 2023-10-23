# When we create a tuple, we normally assign values to it. This is called "packing" a tuple:

# fruits = ("apple", "banana", "cherry")

# But, in Python, we are also allowed to extract the values back into variables. This is called "unpacking"


fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits # assigned value like destructuring

print(green)
print(yellow)
print(red)

# when we use *variable variable has create list of item
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits # in this case tropic is list which include all item exepted first and last item because it is allready preserve

print(green)
print(tropic)
print(red)