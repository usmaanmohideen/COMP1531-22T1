## D. Importing

Here is a file *foo.py*
```python
def bar(txt):
    return txt

name = 'Ralph'
def editName(string):
    name = string
def getName():
    return name
```

In the same directory we have a file *imp.py*. There are multiple ways we can import and use a function in another file. Discuss each.
```python
import foo
print(foo.bar('hi')) # 1

import foo as fooFile
print(fooFile.bar('hi')) # 2

from foo import bar
print(bar('hi')) # 3

from foo import *
print(bar('hi')) # 4
```

> * #1 This is fine, and is useful when using many functions from an import
> * #2 This is like (#1), except useful when the name of the import is quite generic and could be confused with something else
> * #3 This is often useful when you only need to import very particular functions from a file
> * #4 This is not recommended, this imports a whole number of functions that could conflict with other names in the namespace

Why does the following function not behave as intended?
```python
import foo

print(foo.getName())
foo.editName('Hayden')
print(foo.getName())
```

> Because to edit global variables inside of functions we need to add a global keyword
```python
def editName(string):
    global name
    name = string