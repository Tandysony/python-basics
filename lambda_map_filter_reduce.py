print("\n" + "-"*20 + "1. Lambda fucntion" + "-"*20)
# Lambda function: 
# lambda [para]: [return] 
add = lambda x, y: x+y
print(add(2,3))

print("\n" + "-"*20 + "2. Map function" + "-"*20)
# Map function: apply same function to each element of sequence, returns a list
# map(func, list)
n = [1, 2, 3, 4]
print(list(map(lambda x:x**2, n)))
# List comprehension solution
print([x**2 for x in n])


print("\n" + "-"*20 + "3. Filter function" + "-"*20)
# Filter function: filter items out of a sequence, returns a list
# filter(condition, list)
print(list(filter(lambda x:x>2, n)))
# List comprehension solution
print([x for x in n if x>2])


print("\n" + "-"*20 + "4. Reduce function" + "-"*20)
# reduce function: apply same function to each element of sequence, returns an item, NOT a list
# reduce(function, list)
print(reduce(lambda x,y:x*y, n))