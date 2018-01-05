# List

print("-"*20 + "List" + "-"*20)
#   1. create a new list
x = list()
print(x)
x = ["a", 4.55, "work", "$", 70]
print(x)

#     - list comprehension 
#       [ EXPRESSION for VAR in COLLECTION ]
#       [ EXPRESSION for VAR in COLLECTION if <TEST> and <TEST>]]
x = [y**2 for y in xrange(8) if y>4]
print("1. The list after creating is: {}".format(x))
print("----------------------")

#   2. delete/remove a list or an item
x = ["a", 4.55, "work"] + ["$", 70]
del(x[2])
x.remove(4.55) # must be an item, not index
print("2. The list after deleting and removal is: {}".format(x))
x[:1]=[]
print("2. The list after deleting by assigning is: {}".format(x))
print("----------------------")

#   3. append an item
x = ["a", 4.55, "work"]
x.append("$")
print("3. The list after appending is: {}".format(x))
print("----------------------")

#   4. extend: append a sequence to a list
x = ["a", 4.55, "work"]
y = (1, 2)  # tuple
z = ["$", "DOG"]
x.append(y) # '(1, 2)' will be a single element.
x.append(z) # '["$", "DOG"]' will be a single element.
print("4. The list after extending is: {}".format(x)) # output: 4. The list after extending is: ['a', 4.55, 'work', (1, 2), ['$', 'DOG']]
print("4. The length of the list after extending: {}".format(len(x)))
f = [True, "end"]
x += f
print("4. The list after concatenation is: {}".format(x))
print("4. The length of the list after concatenation is: {}".format(len(x)))
print("----------------------")

#   5. insert: x.insert(index, item)
x = ["a", 4.55, "work"]
y = (1, 2)  # tuple
x.insert(1, y)
print("5. The list after inserting is: {}".format(x))
print("----------------------")

#   6. pop: pop the last element out
#       LIFO (without index) 
x = ["a", 4.55, "work", "$", "7"]
lifo_elem = x.pop()
print("6. The lifo element is: {}".format(lifo_elem))
x.pop(2)
print("6. The list after popping is: {}".format(x))
print("----------------------")

#   7. reverse: reverse the order of the list
x = ["a", 4.55, "work"]
x.reverse()
print("7. The list after reverse is: {}".format(x))
print("----------------------")

#   8. sort
#       x.sort() put the items of x in sorted order (sorted in place)
#       sorted(x) returns a NEW sorted list without changing the original list x.
x = ["a", 4.55, "work", "$"]
x.sort()
print("8. The list after sort is: {}".format(x))


## SUMMARY
# 1. List is a sequence type (ordered), and is sortable and mutable.
# 2. List can be created by list comprehension.
# 3. Two ways to delete an element in a list: 'del(el)' or 'list.remove(el)'. The 'el' must be an element not an index. To insert an element to a list, use 'list.insert(idx, el)'.
# 4. 'list.pop()' wont take any parament.
# 5. 'x.sort()' is in-place sorting, while 'sort(x)' returns a new list.