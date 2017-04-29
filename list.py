# List can be an element of another list
init_list = [67, "cherry"]
my_list = ["apple", "pear", 1, init_list]
my_list.append("banana")
print("The list after appending: %s" % my_list)
print("----------------------")

# LIFO , pop the last element out
lifo_elem = my_list.pop()
print("The lifo element is: %s" % lifo_elem)
print("----------------------")

# pop the chossen element
my_elem = my_list.pop(2)
print(my_elem)
print(my_list)
print("----------------------")

# insert
my_elem = my_list.insert(2, "peach")
print(my_list)

# remove a few element
my_list[1:3] = []
print(my_list)
