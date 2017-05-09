
print("-"*20 + "List" + "-"*20)
# List: seqence type, sortable, mutable, 
#   1. create a new list
x = list()
print(x)
x = ["a", 4.55, "work", "$", 70]
print(x)
x = [y**2 for y in range(8) if y>4] # list comprehension
print("1. The list after creating is: %s" %x)
print("----------------------")

#   2. delete/remove a list or an item
x = ["a", 4.55, "work"] + ["$", 70]
del(x[2])
x.remove(4.55) # must be an item, not index
print("2. The list after deleting and removal is: %s" %x)
x[:1]=[]
print("2. The list after deleting by assigning is: %s" %x)
print("----------------------")

#   3. append an item
x = ["a", 4.55, "work"]
x.append("$")
print("3. The list after appending is: %s" % x)
print("----------------------")

#   4. extend: append a sequence to a list
x = ["a", 4.55, "work"]
y = (1, 2)  # tuple
x.append(y)
print("4. The list after extending is: %s" % x)
print("4. The length of the list after extending: %s" %len(x))
print("----------------------")

#   5. insert: x.insert(index, item)
x = ["a", 4.55, "work"]
y = (1, 2)  # tuple
x.insert(1, y)
print("5. The list after inserting is: %s" % x)
print("----------------------")

#   6. pop: pop the last element out
#       LIFO (without index) 
x = ["a", 4.55, "work", "$", "7"]
lifo_elem = x.pop()
print("6. The lifo element is: %s" % lifo_elem)
x.pop(2)
print("6. The list after popping is: %s" % x)
print("----------------------")

#   7. reverse: reverse the order of the list
x = ["a", 4.55, "work"]
x.reverse()
print("7. The list after reverse is: %s" % x)
print("----------------------")

#   8. sort
#       x.sort() put the items of x in sorted order (sorted in place)
#       sorted(x) returns a NEW sorted list without changing the original list x.
x = ["a", 4.55, "work", "$"]
x.sort()
print("8. The list after sort is: %s" % x)