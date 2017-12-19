import sys

# 'int' type
int_max = sys.maxint
print("max int in this system is: {} -- {}.".format(int_max, type(int_max)))

# 'long' type (not available in Python 3)
print(type(int_max+1))
s_long = 48L
print("s_long is: {} -- {}".format(s_long, type(s_long)))

# 'float' type
f = 2.71828182
print("'f' is: {} -- {}".format(f, type(f)))

# 'complex' type
cplx = 2.6 +5j
print("'cplx' is: {} -- {}".format(cplx, type(cplx)))
print("Its real part is {}, and the imaginary part is {}".format(cplx.real, cplx.imag))

# using ** to calculate powers 
result = 2 ** 4
print(result)

# You can assign many varables at once
one, two, three = 1, "two", 3.0
print("one = {}, two = {}, three = {}".format(one, two, three))

# round up
print(round(14.99, 1)) 


## SUMMARY
# 1. There are 3 types of numbers in Python 2.7: 'int', 'long', 'float' & 'complex'. While, in Python 3, 'long' is no long available.
# 2. 'int' will be converted to 'long' if it overflows
# 3. Add an 'L' at the end of the int value to enforce a 'long' type
# 4. User 'x.real' and 'x.imag' to get real part and imaginary part respectively, for a complex number 'x'.