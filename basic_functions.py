# write Fibonacci series up to n
def fib(n):
    '''print Fibonacci series up to n'''
    a, b = 0, 1
    while a < n:
        print (a)
        a, b = b, a+b 

result = fib(20)


def fib2(n):
    '''print Fibonacci series up to n'''
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result

print(fib2(11))

print ("-"*40)


#  Keyword Arguments in a function
def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print "-- This parrot wouldn't", action,
    print "if you put", voltage, "volts through it."
    print "-- Lovely plumage, the", type
    print "-- It's", state, "!"

parrot('a thousand', state='pushing up the daisies', action='smell')  # 1 positional, 2 keyword

print ("-"*40)

# Unpacking Argument: using * operattor to unpack list or tuple
args = [3,4,5]
