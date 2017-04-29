# if statement
# x = int(raw_input("Please enter an integer: "))
x = 10

if x < 0:
    x = 0
    print("Negative value changed to zero")
elif x == 0:
    print(0)
else:
    print("positive value: %d" % x)
print ("-----------------")

# for statement
words = ['cat', 'dog', "bird"]

for w in words:
    print(w, len(w))
print ("-----------------")

# range(start, stop, step) or range(stop): 
# iterate over a sequence of number from "start" to "stop-1" with "step" 
# range() returns a LIST object
# xrange() returns a xrange() object [yielding technique], and it is more efficient
print(range(0, 10, 2))
print(xrange(10))

song = ['Mary', 'has', 'a', 'little', 'lamb']
for i in range(len(song)):
    print(i, song[i])
print ("-----------------")

# break and continue Statements
for i in range(10):
    if i >= 5:
        break
    else:
       print i

