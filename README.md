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
