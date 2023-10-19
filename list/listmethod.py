list=[8,5,5,7,7,6,488,5]

# copy()	Returns a copy of the list
conpyList=list.copy()
# print(conpyList)

# count()	Returns the number of elements with the specified value
print(list.count(5))

# index()	Returns the index of the first element with the specified value
print(list.index(7))

# insert()	Adds an element at the specified position
list.insert(0,999)

# pop()	Removes the element at the specified position
list.pop(0)

# remove()	Removes the first item with the specified value
list.remove(7)

# reverse()	Reverses the order of the list
list.reverse()

# sort()	Sorts the list
list.sort()

# append()	Adds an element at the end of the list
list.append(999)

# extend()	Add the elements of a list (or any iterable), to the end of the current list
list2=["tiger","amit"]
list.extend(list2)

# clear()	Removes all the elements from the list
list2.clear()
print(list2)