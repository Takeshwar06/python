# normal creation of dict
info={
    "name":"deepanshu",
    "age":21,
    "surname":"sinha"
}

#Create a dictionary with 3 keys, all with the value 0:
x = ('key1', 'key2', 'key3')
y = 0

thisdict = dict.fromkeys(x, y)

print(thisdict)