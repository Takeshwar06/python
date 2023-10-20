mydict={
    "name":"tiger",
    "age":21,
    "surname":"janghel"
}

# copy()	Returns a copy of the dictionary
anotherDict=mydict.copy()
# print(anotherDict)

# fromkeys()	Returns a dictionary with the specified keys and value
x = ('key1', 'key2', 'key3')
y = 3
thisdict = dict.fromkeys(x, y)

# print(thisdict)

# get()	Returns the value of the specified key
print(mydict.get("name"))

# items()	Returns a list containing a tuple for each key value pair
print(mydict.items())

# keys()	Returns a list containing the dictionary's keys
print(mydict.keys())

# pop()	Removes the element with the specified key
mydict.pop("surname")
# print(mydict)

# popitem()	Removes the last inserted key-value pair
mydict.popitem()
# print(mydict)

# setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
mydict.setdefault("age",21)
mydict.setdefault("surname","janghel")
# print(mydict)

# update()	Updates the dictionary with the specified key-value pairs if not present field insert key value pair
mydict.update({"age":32})
# print(mydict)

# values()	Returns a list of all the values in the dictionary
print(mydict.values())

# clear()	Removes all the elements from the dictionary
mydict.clear()
print(mydict)