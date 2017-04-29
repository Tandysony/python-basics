# SEQUNCES -- String, List, Tuple
# 1. indexing [i]
x = "My name is Tandysony"
print(x[3])
print("-"*40 + "1")

# 2. slicing [start : end+1 : step]
print(x[1:4])
print(x[1:10:2])
print(x[3:])
print(x[:4])
print(x[-3:])
print("-"*40 + "2")

# 3. adding/concatenating 
x = "My name is" + " Tandysony"
print(x)
y= ["pig", "cow"] + ["sheep"]
print(y)
print("-"*40 + "3")

# 4. multiflying
x = [8, 6, 3] * 3
print(x)
print("-"*40 + "4")

# 5. check membership
x = "Tandysony"
print ("s" not in x)

y= ["pig", "cow"]
print ("pig" in y)
print("-"*40 + "5")

# 6. iterating
x = [6, 8, 4]
for index, item in enumerate(x):
    print(index, item)
print("-"*40 + "6")

# 7. number of items
x = [6, 8, 4]
print(len(x))
print("-"*40 + "7")

# 8. minimum, maximum and sum
x = ["pig", "cow", "sheep"]
print(min(x))
print(max(x))
y = [6, 8, 4, 9]
print(sum(y))
print(sum(y[2:]))
print("-"*40 + "8")

# 9. sorting: returns a new list
x = ["pig", "cow", "sheep"]
print(sorted(x))
print("-"*40  + "9")

# 10. count (item)
x = "tandysony"
print(x.count("n"))
y = ["pig", "cow", "sheep", "cow2", "sheep"]
print(y.count("sheep"))
print("-"*40 + "10")

# 11. index (item)
x = "tandysony"
print(x.index("n"))
y = ["pig", "cow", "sheep", "cow2", "sheep"]
print(y.index("sheep"))
print("-"*40 + "11")

# 12. unpacking: the numner of variables must exactly match the lenth of the list
y = ["pig", "cow", "sheep", "cow2", "sheep"]
a, b, c, d, e = y
print(d)
print("-"*40 + "12")