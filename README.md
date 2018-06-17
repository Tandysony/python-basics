# python-basics

Re-learning python basics

## Basic Concepts

- `[]`: brackets or square braces. Lists are enclosed in brackets.
- `()`: parentheses. Tuples are enclosed in parentheses.
- `{}`: curly braces. Dictionaries are enclosed in curly braces, and values can be assigned and accessed using square braces, e.g., `dict[2]` or `dict["id"]`.
- `**`: exponent − Performs exponential (power) calculation on operators. `a**b` means `10` to the power `20` if `a = 10` and `b = 20`.
- `//`: floor division. The division of operands where the result is the quotient in which the digits after the decimal point are removed.
- `is`: Evaluates to true if the variables on either side of the operator **point to the same object** and false otherwise. `x is y`, here `is` results in `1` if `id(x)` equals `id(y)`.

For fundamentals, refer to [this post](https://www.tutorialspoint.com/python/python_interview_questions.htm).

## 1. What are the python processing mode in python?

- `r` for reading only
- `r+` opens for reading and writing (cannot truncate a file)
- `w` for writing only
- `w+` for writing and reading (can truncate a file)
- `rb` for reading a binary file. The file pointer is placed at the beginning of the file.
- `rb+` reading or writing a binary file
- `wb+` writing a binary file
- `a+` opens for appending
- `ab+` Opens a file for both appending and reading in binary. The file pointer is at the end of the file if the file exists. The file opens in the append mode.
- `x` open for exclusive creation, failing if the file already exists (Python 3)

## 2. Explain the ternary operator in Python.

- `[on True] if [expression] else [on False]`

```python
a,b = 1,2
min = b if a>b else a

print(c) # 1
```

In javascript,

```js
const a = 1,
  b = 2;
const min = a > b ? b : a;
console.log(min); // 1
```

## 3. How is multithreading achieved in Python?

A thread is a lightweight process, and multithreading allows us to execute multiple threads at once. As you know, Python is a multithreaded language. It has a multi-threading package.

The GIL (Global Interpreter Lock) ensures that a single thread executes at a time. A thread holds the GIL and does a little work before passing it on to the next thread. This makes for an illusion of parallel execution. But in reality, it is just threads taking turns at the CPU. Of course, all the passing around adds overhead to the execution.

I have used multi-thread in Email sending module in previous project:

```python
from email.mime.image import MIMEImage # Multipurpose Internet Mail Extensions (MIME)
from threading import Thread
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template

class EmailThread(Thread):
    def __init__(self, sender, to, subject='', body='', html_content='', reply_to=None, cc=None):
       ...

        Thread.__init__(self)

    def run(self):
        _send(self.sender, self.recipient_list, self.subject, self.message, self.html_content, self.reply_to, self.cc)

def _send(sender, to, subject='', body='', html_content='', reply_to=None, cc=None):
    if not isinstance(to, (list, tuple)):
        to = (to,)
    ...

    message.mixed_subtype = 'related'  # This is critical, otherwise images will be displayed as attachments!
    ...
    img.add_header('Content-ID', '<rndgo-logo>')
    img.add_header('Content-Disposition', 'inline', filename='filename')
    message.attach(img)
```

Using Gmail smtp server to send transitional mails:

```python
MAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_HOST_USER=your_gmail_account
EMAIL_HOST_PASSWORD=your_gmail_pwd
EMAIL_USE_TLS=True
```

Do forget enable your at your Gmail account for this feature.

## 4. Explain inheritance.

When one class inherits from another, it is said to be the child/derived/sub class inheriting from the parent/base/super class. It inherits/gains all members (attributes and methods).

Inheritance lets us reuse our code, and also makes it easier to create and maintain applications. Python supports the following kinds of inheritance:

- Single Inheritance - A class inherits from a single base class.
- Multiple Inheritance - A class inherits from multiple base classes.
- Multilevel Inheritance - A class inherits from a base class, which, in turn, inherits from another base class.
- Hierarchical Inheritance - Multiple classes inherit from a single base class.
- Hybrid Inheritance- Hybrid inheritance is a combination of two or more types of inheritance.

## 5. How is memory managed in Python?

Python has a **private heap space** to hold all objects and data structures. Being programmers, we cannot access it; it is the interpreter that manages it. But with the core API, we can access some tools. The Python memory manager controls the allocation.

Additionally, an inbuilt **garbage collector** recycles all unused memory so it can make it available to the heap space.

## 6. Explain help() and dir() functions in Python.

The `help()` function displays the documentation string and help for its argument. The `dir()` function displays all the members of an object(any kind).

## 7. Whenever you exit Python, is all memory de-allocated?

The answer here is no. The modules with circular references to other objects, or to objects referenced from global namespaces, aren’t always freed on exiting Python.

Plus, it is impossible to de-allocate portions of memory reserved by the C library.

## 8. What is a dictionary in Python?

Dictionary holds key-value pairs, similar to javascript `object`. A dictionary is mutable, and we can also use a comprehension to create it.

## 9. What do you mean by `*args` and `**kwargs`?

In cases when we don’t know how many arguments will be passed to a function, like when we want to pass a list or a tuple of values, we use `*args`.

```python
def func(*args):
    for i in args:
        print(i)  

func(3,2,1,4,7) # <-- arguments
```

`**kwargs` takes keyword arguments when we don’t know how many there will be.

```python
def func(**kwargs):
    for i in kwargs:
        print(i,kwargs[i])

func(a=1,b=2,c=7) # <-- keyword arguments
```

The words `args` and `kwargs` are convention, and we can use anything in their place.

## Coding

## 10. Write Python logic to count the number of capital letters in a file.

```python
import os

file = os.path("path/to/the/file")
with open(file,'r') as myFile:
    count = 0
    for i in myFile:
        if i.isupper():
            count++

    print(count)
```

## 11. How would you randomize the contents of a list in-place?

```python
from random import shuffle

shuffle(myList)
```

## 12. How will you set the starting value in generating random numbers?

```python
import random

random.seed( 10 )
print "Random number with seed 10 : ", random.random()

# It will generate same random number
random.seed( 10 )
print "Random number with seed 10 : ", random.random()

# It will generate same random number
random.seed( 10 )
print "Random number with seed 10 : ", random.random()
```

## 13. What is the difference between `del()` and `remove()` methods of list?

To remove a list element, you can use either the `del` statement **if you know exactly which element(s) you are deleting** or the `remove()` method **if you do not know**.

## 14. Function and method for `list`?

**String special operators:**

- `+` Concatenation - Adds values on either side of the operator

- `*` Repetition - Creates new strings, concatenating multiple copies of the same string

- `[]` Slice - Gives the character from the given index

- `[ : ]` Range Slice - Gives the characters from the given range

- `in` Membership - Returns true if a character exists in the given string

- `not in` Membership - Returns true if a character does not exist in the given string

- `r/R` Raw String - Suppresses actual meaning of Escape characters. The syntax for raw strings is exactly the same as for normal strings with the exception of the raw string operator, the letter "r," which precedes the quotation marks. The "r" can be lowercase (r) or uppercase (R) and must be placed immediately preceding the first quote mark.

- `%` Format - Performs String formatting See at next section

**Built in functions:**

- `cmp(list1, list2)`: Compares elements of both lists.

- `len(list)`: Gives the total length of the `list`.

- `max(list)`: Returns item from the `list` with `max` value.

- `min(list)`: Returns item from the `list` with `min` value.

- `list(seq)`: Converts a `tuple` into `list`.

**Built in methods:**

- `list.append(obj)`: Appends object `obj` to `list`

- `list.count(obj)`: Returns count of how many times `obj` occurs in `list`

- `list.extend(seq)`: Appends the contents of `seq` to `list`

- `list.index(obj)`: Returns the lowest index in `list` that `obj` appears

- `list.insert(index, obj)`: Inserts object `obj` into `list` at offset index

- `list.pop(obj=list[-1])`: Removes and returns last object or `obj` from `list`

- `list.remove(obj)`: Removes object `obj` from `list`

- `list.reverse()`: Reverses objects of `list` in place

- `list.sort([func])`: Sorts objects of `list`, use `compare` func if given

## 15. Function and method for strings.

- `capitalize(str)`: Capitalizes first letter of string.

- `isalnum(str)`: Returns `True` if string has **at least 1 character** and **all characters are alphanumeric** and false otherwise.

- `isdigit(str)`: Returns true if string contains **only digits** and false otherwise.

- `islower(str)`: Returns true if string has **at least 1 cased character** and all cased characters are **in lowercase** and false otherwise.

- `isupper()`: Returns true if string has at least one cased character and all cased characters are in uppercase and false otherwise.

- `isnumeric()`: Returns true if a unicode string contains only numeric characters and false otherwise.

- `isspace()`: Returns true if string contains **only whitespace characters** and false otherwise.

- `istitle()`: Returns true if string is properly "titlecased", e.g. "This Is Titlecased", and false otherwise.

- `str.join(seq)`: Merges (concatenates) the string representations of elements in sequence `seq` into a string, with separator string.

- `len(str)`: Returns the length of the string.

- `str.ljust(width[, fillchar])`: Returns a space-padded string with the original string left-justified to a total of width column.

- `str.lower()` or `upper()`: Converts all uppercase letters in string to lowercase, or the other way around.

- `str.lstrip()`: Removes all leading whitespace in string.

- `max(str)`: Returns the max alphabetical character from the string `str`.

- `min(str)`: Returns the min alphabetical character from the string `str`.

- `str.replace(old, new [, max])`: Replaces all occurrences of `old` in string with new or at most `max` occurrences if `max` given.

- `strip([chars])`: Performs both `lstrip()` and `rstrip()` on string.

- `str.swapcase()`: Inverts case for all letters in string.

- `str.title()`: Returns "titlecased" version of string, that is, all words begin with uppercase and the rest are lowercase.

## 16. `random` package for random date generating

- `choice(seq)`: Returns a random item from a list, tuple, or string.

- `randrange([start,] stop [,step])`: returns a randomly selected element from `range(start, stop, step)`, e.g., `randrange(0, 101, 2)` returns a random odd integer from 1 to 100 inclusive

- `random()`: returns a random float `r`, such that `0` is less than or equal to `r` and `r` is less than `1`.

- `seed([x])`: Sets the integer starting value used in generating random numbers. Call this function before calling any other random module function.

- `sample(range(1000), 8)`: 8 random samples without replacement.

## 17. JSON data in Python

1.  To work with a JSON string object, use "json.loads(), json.dumps()". Pay attention to the 's' before the left parentheses
2.  The JSON decoder and endcoder are illustrated below:

**JSON Decoder**

| JSON          | Python    |
| ------------- | --------- |
| object        | dict      |
| array         | list      |
| string        | unicode   |
| number (int)  | int, long |
| number (real) | float     |
| true          | True      |
| false         | False     |
| null          | None      |

**JSON Encoder**

| Python           | JSON   |
| ---------------- | ------ |
| dict             | object |
| list, tuple      | array  |
| str, unicode     | string |
| int, long, float | number |
| True             | true   |
| False            | false  |
| None             | null   |

3.  When load and dump JSON files, use `json.load()`, `json.dump()`
4.  If `open('file_path')` raises `IOError: [Error 2] No such file or directory: 'aa.bb'`, use `getcwd()` to double check the current working directory.

## 18. Class and subclass

- Do not forget constructor `__init__`
- The `__str__` is a special built-in method can be overridden.
- When calling a method, do not forget `()` at the end.

```python
# base class
class Pet(object):
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def getName(self):
        return self.name

    def getSpecies(self):
        return self.species

    def __str__(self):
        return ("{0} is a {1}".format(self.name, self.species))

polly = Pet("Polly", "Parrot")
print(polly)

pet_name = polly.getName()
print(pet_name)


# sub-class
class Dog(Pet):
    def __init__(self, name, chases_cats):
        Pet.__init__(self, name, "Dog")
        self.chases_cats = chases_cats

    def chasesCats(self):
        return self.chases_cats

rommy = Dog("Rommy", True)
print(rommy.getSpecies())
print(rommy.chasesCats())
print("Does {0} , the {1}, chase cats? {2}".format(rommy.getName(), rommy.getSpecies(), rommy.chasesCats() ))
```
