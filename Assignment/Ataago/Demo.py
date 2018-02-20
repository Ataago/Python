1
A:

list1 = [1, -3, -5, 4, -7, 2, 0, 3]

count = 0
for i in range(0, len(list1)):
    if list1[i] < 0:
        list1[i] = -1
        count += 1
for i in range(0, count):
    list1.remove(-1)

for i in range(0, len(list1)):
    for j in range(i + 1, len(list1)):
        if list1[i] > list1[j]:
            temp = list1[i]
            list1[i] = list1[j]
            list1[j] = temp

print(list1)

output:
[0, 1, 2, 3, 4]

1
B:


class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


s = Stack()

print(s.isEmpty())
s.push("hello")
s.push('Shubham')
print(s.peek())
s.push("Kumar")
print(s.size())
print(s.isEmpty())
s.push(617)
print(s.pop())
print(s.pop())
print(s.size())

output:

True
Shubham
3
False
617
Kumar
2

2
A:

Loop
control
statements
change
execution
from its normal

sequence.When
execution
leaves
a
scope, all
automatic
objects
that
were
created in that
scope
are
destroyed.Python
supports
the
following
control
statements.
Continue
Statement
It
returns
the
control
to
the
beginning
of
the
loop.

# Prints all letters except 'e' and 's'
for letter in 'geeksforgeeks':
    if letter == 'e' or letter == 's':
        continue
    print
    'Current Letter :', letter
    var = 10

Output:

Current
Letter: g
Current
Letter: k
Current
Letter: f
Current
Letter: o
Current
Letter: r
Current
Letter: g
Current
Letter: k
Break
Statement
It
brings
control
out
of
the
loop

for letter in 'geeksforgeeks':

    # break the loop as soon it sees 'e' 
    # or 's'
    if letter == 'e' or letter == 's':
        break

print
'Current Letter :', letter

Output:

Current
Letter: e

Pass
Statement
We
use
pass
statement
to
write
empty
loops.Pass is also
used
for empty control statement, function and classes.

# An empty loop
for letter in 'geeksforgeeks':
    pass
print
'Last Letter :', letter
Run
on
IDE
Output:

Last
Letter: s

3
A:


def reverse(s):
    str = ""
    for i in s:
        str = i + str
    return str


s = "Shubhamk617"

print("The original string  is : ", end="")
print(s)

print("The reversed string(using function) is : ", end="")
print(reverse(s))

output:
The
original
string is: Shubhamk617
The
reversed
string(using
function) is: 716
kmahbuhS


def reverseMe(str):
    rstr = ''
    l = len(str)
    while l:
        l -= 1
        rstr += str[l]
    return rstr


s = "shubhamk617"
print("The original string  is : ", end="")
print(s)

print("The reversed string(using function) is : ", end="")
print(reverseMe(s)

output:
The
original
string is: Shubhamk617
The
reversed
string(without
using
function) is: 716
kmahbuhS

3
B:


def Range(list1):
    largest = list1[0]
    largest2 = list1[0]
    for item in list1:
        if item > largest:
            largest = item
        elif largest2 != largest and largest2 < item:
            largest2 = item

    print("Largest element is:", largest)
    print("Second Largest element is:", largest2)


list1 = [12, 45, 2, 41, 31, 10, 8, 6, 4]
Range(list1)

output:
Largest
element is: 45
Second
Largest
element is: 41

4
A:

Data
types in Python
Every
value in Python
has
a
datatype.Since
everything is an
object in Python
programming, data
types
are
actually
classes and variables
are
instance(object)
of
these
classes.

There
are
various
data
types in Python.Some
of
the
important
types
are
listed
below.

Python
Numbers
Integers, floating
point
numbers and complex
numbers
falls
under
Python
numbers
category.They
are
defined as int, float and complex


class in Python.


We
can
use
the
type()
function
to
know
which


class a variable or a value belongs to and the isinstance() function to check if an object belongs to a particular class.


a = 5
print(a, "is of type", type(a))

a = 2.0
print(a, "is of type", type(a))

a = 1 + 2j
print(a, "is complex number?", isinstance(1 + 2j, complex))

Integers
can
be
of
any
length, it is only
limited
by
the
memory
available.

A
floating
point
number is accurate
up
to
15
decimal
places.Integer and floating
points
are
separated
by
decimal
points.
1 is integer, 1.0 is floating
point
number.

Complex
numbers
are
written in the
form, x + yj, where
x is the
real
part and y is the
imaginary
part.Here
are
some
examples.

>> > a = 1234567890123456789
>> > a
1234567890123456789
>> > b = 0.1234567890123456789
>> > b
0.12345678901234568
>> > c = 1 + 2j
>> > c
(1 + 2j)

Python
List
List is an
ordered
sequence
of
items.It is one
of
the
most
used
datatype in Python and is very
flexible.All
the
items in a
list
do
not need
to
be
of
the
same
type.Declaring
a
list is pretty
straight
forward.Items
separated
by
commas
are
enclosed
within
brackets[].

>> > a = [1, 2.2, 'python']
We
can
use
the
slicing
operator[]
to
extract
an
item or a
range
of
items
from a list.Index
starts
form
0 in Python.

a = [5, 10, 15, 20, 25, 30, 35, 40]

# a[2] = 15
print("a[2] = ", a[2])

# a[0:3] = [5, 10, 15]
print("a[0:3] = ", a[0:3])

# a[5:] = [30, 35, 40]
print("a[5:] = ", a[5:])

>> > a = [1, 2, 3]
>> > a[2] = 4
>> > a
[1, 2, 4]

Python
Tuple
Tuple is an
ordered
sequence
of
items
same as list.The
only
difference is that
tuples
are
immutable.Tuples
once
created
cannot
be
modified.

Tuples
are
used
to
write - protect
data and are
usually
faster
than
list as it
cannot
change
dynamically.

It is defined
within
parentheses()
where
items
are
separated
by
commas.

>> > t = (5, 'program', 1 + 3j)
We
can
use
the
slicing
operator[]
to
extract
items
but
we
cannot
change
its
value.
String is sequence
of
Unicode
characters.We
can
use
single
quotes or double
quotes
to
represent
strings.Multi - line
strings
can
be
denoted
using
triple
quotes, ''' or """.

>>> s = "This is a string"
>>> s = '''
a
multiline
Like
list and tuple, slicing
operator[]
can
be
used
with string.Strings are immutable.
Python
Set
Set is an
unordered
collection
of
unique
items.Set is defined
by
values
separated
by
comma
inside
braces
{}.Items in a
set
are
not ordered.

Python
Dictionary
Dictionary is an
unordered
collection
of
key - value
pairs.

It is generally
used
when
we
have
a
huge
amount
of
data.Dictionaries
are
optimized
for retrieving data.We must know the key to retrieve the value.

In
Python, dictionaries
are
defined
within
braces
{}
with each item being a pair in the form key:value.Key and value
can
be
of
any
type.

>> > d = {1: 'value', 'key': 2}
>> > type(d)
<

class 'dict'>


5:

num = int(input("Enter a number: "))

factorial = 1

if num < 0:
    print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    for i in range(1, num + 1):
        factorial = factorial * i
    print("The factorial of", num, "is", factorial)
rev = 0
while (factorial > 0):
    dig = factorial % 10
    rev = rev * 10 + dig
    factorial = factorial // 10
print("Reverse of the number:", rev)

output:
Enter
a
number: 4
The
factorial
of
4 is 24
Reverse
of
the
number: 42

6:

Operator
Description
Example
+                    Concatenation - Adds
values
on
either
side
of
the
operator
a + b
will
give
HelloPython
*				Repetition - Cre
tes
new strings, concatena
ing mult
ple co
ies of
the
same st
i n g
a*2
will gi ve -HelloHello
[]					Slice - G
ves
the chara
ter from the g

ven i
dex	a
[1]
will
give e
[ :                ]				Range Slice
- G
ves the ch
racters from t

e giv
n range	a[1:
4]
will give ell
in					Members
ip - Retu
ns true if a character
exists
in the
given
string	H in a will give 1
not in				Members
ip - Retu
ns true if a c
aracter does not
exist
in the
given stri
g	M
not in a wi ll
gi
e 1
r/R					Raw Str
ng - S
ppresses a
tual m
aning of Esape
charac
ers. The syntax for raw strings is exactly the same as for normal strings with the exception of the raw string operator, the letter "r," which precedes thequotation marks. The "r" can be lowercase (r) or uppercase (R) and must be placed immediately preceding the frst quote mark.	print r'\n' prints \n and print R'\n' prints \n
%					For
at - Perfo
ms
Str
ng f
rmatting
See at next s
cti
n


i ask nuthing but a treat...!!!