# Tutorial 4

## A. Code Review

**This exercise links to [Lab04 - Code Review](https://gitlab.cse.unsw.edu.au/COMP1531/22T1/STAFF/repos/lab04/lab04_code-review)**.

In project groups, discuss the two pieces of code and decide as a group which one you think has better style.

## B. Pylint

Pick one of `review_1.py` and `review_2.py` and run it through pylint. Consider what issues it highlights and discuss, as a class, the alternatives for resolving them.

* Fixing the code so the issue no longer exists.
* Adding a pragma to the line the issue occurs, so pylint stops reporting it.
* Suppressing all instances of such errors via a config file.

> Some helpful commands
> * `pylint review_1.py`
> * `pylint review_1.py --disable=no-module-docstring`
> * `pylint review_1.py --disable=no-module-docstring --generate-rcfile > .pylintrc`

## C. Software Verification

### Part 1 - Finding a Defect

**This exercise links to [Lab04 - Verification](https://gitlab.cse.unsw.edu.au/COMP1531/22T1/STAFF/repos/lab04/lab04_verification)**.

* As a class, write a failing unit test which catches the bug.
* In project groups, trace through the code **without running it**, and propose a fix to the code.

### Part 2 - Coverage Checking

Your tutor will demonstrate how to run coverage by running it on `day_to_year.py`.

> `coverage run --source=. -m pytest` or `coverage run -m pytest` for short.
>
> Access reports via `coverage report` and `coverage html`.

## C. The Object Model

**This exercise links to [Lab04 - Tamagotchi](https://gitlab.cse.unsw.edu.au/COMP1531/22T1/STAFF/repos/lab04/lab04_tamagotchi)**.

Without looking at the source code inside `tamagotchi.py`, look at the interface for the `Tamagotchi` class.

```
Help on class Tamagotchi in module tamagotchi:

class Tamagotchi(builtins.object)
 |  Tamagotchi(name)
 |
 |  Represents a single Tamagotchi pet.
 |
 |  Methods defined here:
 |
 |  __init__(self, name)
 |      Given a name, initialises a Tamagotchi as though born with basic stats.
 |
 |  __str__(self)
 |      Returns a string representing the current status of the tamagotchi.
 |
 |  feed(self)
 |      Decreases the Tamagotchi's hunger level.
 |
 |  increment_time(self)
 |      Adjusts stats as though time has passed for this tamagotchi.
 |
 |  is_dead(self)
 |      Returns True if the Tamagotchi is dead, False otherwise.
 |
 |  play(self)
 |      Decreases the Tamagotchi's boredom level.
```

You can access the above via invoking the [`help`](https://docs.python.org/3/library/functions.html#help) function on the `Tamagotchi` class.

Create a new Tamagotchi object and invoke some of its methods.

As you write the solution, discuss:
* What is the difference between a module, a class, and a function?

> Module: a python file
>
> Class: an object type definition
>
> Function: A kind of object that allows you to give inputs and receive outputs (you can show them that functions themselves are objects in memory by printing out a function)

* What is the difference between normal function and a method of an object?

> Normal function - lives in a python program (accessed with `module.function()`)
>
> Method of an object - lives inside the object (accessed with `object.method()`)

> A friendly note for tutors from Nick
>
> PLEASE try to keep this simple and straightforward - at this point in the course we are treating objects as black boxes in the sense that they're not expected to know how they work internally or how to make their own classes or anything about OOP.

At the moment it's just about the idea of 'The Object Model' in an abstract sense (entities/objects/types, methods and attributes) which we want to get them comfortable with

## E. More Python Practice

Write a program [prettydate.py](prettydate.py) that converts 24 hour time into 12 hour time.
- You may assume that all inputs will be a valid 24 hour time.
- You program should read each line of input from standard input until EOF and output the result to standard output.

Sample input:
```python
1234
0525
0000
0001
1904
```

Sample output:
```python
12:34 PM
05:25 AM
00:00 AM
00:01 AM
07:04 PM
```

*Ensure pylint is run on your code.*

Make your code as pythonic as possible.

> See [prettydate.py](solutions/prettydate.py).
