
# Tuple: 
#   * seqence type, support all operations for sequences.
#   * immutable, but member objects may be mutable. 
#   * userful for fixed data, faster than Lists
#   * If the contents of a list shouldn't change, use a tuple to prevent items from accidently being added, changed, or deleted

#   1. create a new tuple
print("\n\n" + "-"*20 + "1. create a new tuple" + "-"*20)
list_1 = [1, "dog", "&"]
x = ()  # empty tuple
x = (1, 2, 3)
x = 1, # single-item tuple. The comma "," must be there, otherwise it is an integer 
x = "a", 4.55, "work", "$", 70  # parenthesis are optional
print(x)
x = tuple(list_1) # tuple from a list
print(x)

#   2. immutable: but member objects may be mutable. 
print("\n\n" + "-"*20 + "2. immutable: but member objects may be mutable." + "-"*20)
x = ([1,2], 3)  # 2-item tuple: list and int
del(x[0][1]) # ([1], 3)
print("The tuple after operation is: %s" % (x,)) # PAY ATTENTION TO THE "(X,)"
print("The tuple after operation is: %s" % str(x))

x = ("a", 4.55, "work", "$", 70)
del(x[1])   # error!
x[1] = 9    # error!