
# Sets: store non-duplicate items, does not support indexing
# very fast access v.s. Lists, math set operations (union, intersect), unordered
print("#"*20 + " Basic Operations " + "#"*20)
#   1. create a new list
print("-"*20 + "1. create a new set" + "-"*20)
x = {}
x = set()
list_duplicates = ["a", 4.55, "work", "$", 70, "work"]
print("The list with duplicates: %s" %list_duplicates)
x = set(list_duplicates) # new set from list, strips out duplicates
print("The set from list with duplicates: %s" %x)

x = {y**2 for y in range(8) if y>4} # set comprehension
print("The set after creating is: %s" %x)

#   2. Add an item
print("\n\n" + "-"*20 + "2. Add an item" + "-"*20)
x = {3, "good", '$'}
x.add(7) # no index for set
print("The set after adding is: %s" %x)

#   3. Remove an item
print("\n\n" + "-"*20 + "3. remove an item" + "-"*20)
x = {3, "good", '$'}
x.remove("good") # no index, must be a member, otherwise raise KeyError
x.discard("7") # does nothing if not a member
print("The set after removing is: %s" %x)

#   4. Get the lenth
print("\n\n" + "-"*20 + "4. get the length" + "-"*20)
x = {3, "good", '$'}
print("The length of the set: %s" % len(x))

#   5. check the membership in a set
print("\n\n" + "-"*20 + "5. check membership in a set" + "-"*20)
x = {3, "good", '$'}
check = ("s" not in x)
print("'s' is not a member of the set?: %r" % check)


#   6. pop a random item (in the order they appear in the hash table, doesn't like list.pop())
print("\n\n" + "-"*20 + "6. pop a random item" + "-"*20)
x = {"good", 3, '$', 2, "c"}
y=x.pop()
print("The popped element of the set: %s" % y)
y=x.pop()
print("The set after popping: %s" % x)


#   7. delete all items from a set
print("\n\n" + "-"*20 + "7. delete all items from a set" + "-"*20)
x = {"good", 3, '$', 2, "c"}
x.clear()
print("The set after clearing: %s" % x)


# ///////////////////////////////////////////////////////////////////

print("\n\n" + "#"*20 + " Standard Mathmatical Operations " + "#"*20)
x = {"good", 3, '$', 2, "c"}
y = {"good", "c", 77}
print("The set x is %s.\n The set y is %s" % (x,y))

#   8. Intersection ( AND )
print("\n\n" + "-"*20 + "8. Intersection ( AND )" + "-"*20)
result = x & y
print("The Intersection of the two sets is: %s" % result)

#   9. Union ( OR )
print("\n\n" + "-"*20 + "9. Union ( OR )" + "-"*20)
result = x | y
print("The Union of the two sets is: %s" % result)

#   10.  Symemetric diffference ( XOR )
print("\n\n" + "-"*20 + "Symemetric diffference ( XOR )" + "-"*20)
result = x ^ y
print("The Symemetric diffference of the two sets is: %s" % result)

#   11.  Difference ( in set1 but not in set2 )
print("\n\n" + "-"*20 + "11.  Difference ( in set1 but not in set2 )" + "-"*20)
result = x - y
print("The difference of the two sets is: %s" % result)

#   12.  Subset ( set2 constains set1 ): returns a boolean
print("\n\n" + "-"*20 + "12.  Subset ( set2 constains set1 )" + "-"*20)
y = {"good", "c",}
result = (x <= y)
print("Is x a subset of y?: %r" % result)

#   13.  Superset ( set1 constains set2 ): returns a boolean
print("\n\n" + "-"*20 + "13.  Superset ( set1 constains set2 )" + "-"*20)
result = (x >= y)
print("Is x a superset of y?: %r" % result)

