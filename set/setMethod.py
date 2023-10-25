myset={"tiger","amit","bhola"}
print("original set",myset)
# add()	Adds an element to the set
myset.add("takesh")
print(myset)
# clear()	Removes all the elements from the set
# myset.clear()
# print(myset)

# copy()	Returns a copy of the set
copySet=myset.copy()
# print(copySet)

# difference()	Returns a set containing the difference between two or more sets
# Return a set that contains the items that only exist in set x, and not in set y:
z=myset.difference(copySet)

# difference_update()	Removes the items in this set that are also included in another, specified set

# discard()	Remove the specified item
# intersection()	Returns a set, that is the intersection of two other sets
# intersection_update()	Removes the items in this set that are not present in other, specified set(s)
# isdisjoint()	Returns whether two sets have a intersection or not
# issubset()	Returns whether another set contains this set or not
# issuperset()	Returns whether this set contains another set or not
# pop()	Removes an element from the set
# remove()	Removes the specified element
# symmetric_difference()	Returns a set with the symmetric differences of two sets
# symmetric_difference_update()	inserts the symmetric differences from this set and another
# union()	Return a set containing the union of sets
# update()	Update the set with the union of this set and others