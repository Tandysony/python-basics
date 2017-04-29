
# Dict: key/value pair {"key1":value1, "key2":value2}
# Associative array, like Java HashMap, 
# entries in a dict are in random order (unordered)

#  1. create a dict
print("-"*20 + "1. create a dict" + "-"*20)
x = {"beef": 14.76, "pork":7.99, "chicken":10.49} # commonly used
print("x is %s" % x)
y = dict([("beef", 14.76), ("pork", 7.99), ("chicken", 10.49)])
print("y is %s" % y)
z= dict(beef=14.76, pork=7.99, chicken=10.49)
print("z is %s" % z)

#  2. add and change an item
print("\n\n" + "-"*20 + "2. add and change an item" + "-"*20)
x["beef"]=16.99
print("Beef value is %s:" % x["beef"])

#  3. remove an item
print("\n\n" + "-"*20 + "3. remove an item" + "-"*20)
del(x["chicken"])
print("Dict after deleting an item: %s" % x)

#  4. get the length
print("\n\n" + "-"*20 + "4. get the length" + "-"*20)
print("The length of the Dict is: %i" % len(x))

#  5. check membership in a dict (only the keys)
print("\n\n" + "-"*20 + "5. check membership in a dict" + "-"*20)
isMember = "goat" in x
print("Is 'goat' in the dict?: %r" % isMember)

#  6. delete all items from a dict
print("\n\n" + "-"*20 + "6. delete all items from a dict" + "-"*20)
x.clear()
print(x)
del(x)  # delete the dict
#print(x)    # error !

#  7. accessing keys and values
print("\n\n" + "-"*20 + "7. accessing keys and values" + "-"*20)
x = {"beef":18.99, "chicken":16.49, "fish":21.68}
print("All the keys: %s" % x.keys())
print("All the values: %s" % x.values())
print("All the items: %s" % x.items())