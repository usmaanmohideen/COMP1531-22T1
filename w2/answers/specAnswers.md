# Tutorial 2

## Core Exercises

## A. Code Review

[This exercise links to **Lab 02 - Code Review**](https://gitlab.cse.unsw.edu.au/COMP1531/22T1/STAFF/repos/lab02/lab02_code-review).

In groups, discuss answers to the questions. If you have time, you can start modifying the code.

> Issues:
> * Spacing not consistent
> * Indentation not 4 spaces (refer to style guide on webcms3)
> * Could use for-range loop in this case
> * `range(len(x))` is redundant, could just use range normally

> Could make things even shorter:
```python
[(element * 2 if element % 2 == 0 else element) for element in x]
```

## B. Thinking About Testing

* What is a test list? Why is it important?

> Test list - a list of tests that cover the specification cases.
> Test lists are important as they are the basis for the correctness of the system - anything that's left off the test list is a potential defect or bug in the area that's not going to have a test written.

* What is a good approach to writing a test list?

> A systematic approach
https://slides.com/jakerenzella/comp1531-21t3-1-4-testing-intro#/6

[This exercise links to **Lab 02 - Testing**](https://gitlab.cse.unsw.edu.au/COMP1531/22T1/STAFF/repos/lab02/lab02_testing).

Some example tests:

```python
'''
Tests for check_password()
'''
from password import check_password

def test_horrible():
    assert check_password("password") == "Horrible password"
    assert check_password("iloveyou") == "Horrible password"
    assert check_password("123456") == "Horrible password"

def test_poor_less_than_eight():
    assert check_password('only3') == 'Poor password'

def test_poor_no_number():
    assert check_password('nonumberhereohohoho') == 'Poor password'

def test_poor_empty():
    assert check_password('') == 'Poor password'

def test_moderate_no_numbers():
    assert check_password("Idonothaveanynumbers") == "Moderate password"

def test_moderate_no_lowercase():
    assert check_password('IONLYHAVEUPPERCASELETTERSANDNUMBER12345') == 'Moderate password'

def test_moderate_no_uppercase():
    assert check_password('ionlyhavelowercaselettersandnumbers12345') == 'Moderate password'

def test_moderate_minimum():
    assert check_password('Onlygot8chr') == 'Moderate password'

def test_strong():
    assert check_password("MyVerySecurePassword123") == "Strong password"
```

## C. Test-Driven Development

* What is test-driven development? How does it help us write better code?

> 1. Write the stub
> 2. Write the test(s)
> 3. Run the test(s) (they'll fail of course)
> 4. Implement the methods
> 5. Pass the tests

> * Tests are decoupled from implementation
> * We write our code to pass our tests, not the other way around
> * Allows us to conceptualise edge cases more easily when writing a test list

* Complete the stubs inside `test_list_exercises.py` as a class.

```python
from list_exercises import reverse_list, minimum, sum_list

def test_reverse():
    l = ["how", "are", "you"]
    reverse_list(l)
    assert l == ["you", "are", "how"]

def test_min_positive():
    assert minimum([1, 2, 3, 10]) == 1

def test_sum_positive():
    assert sum_list([7, 7, 7]) == 21
```

* In pairs, work on steps 2 and 3 of the exercise.

[This exercise links to **Lab 02 - List**](https://gitlab.cse.unsw.edu.au/COMP1531/22T1/STAFF/repos/lab02/lab02_list).

## D. Fixtures

```python
import pytest

@pytest.fixture
def lst():
    return [1, 2, 3, 4, 5]

def test_reverse(lst):
    reverse_list(l)
    assert l == [5, 4, 3, 2, 1]

def test_min_positive(lst):
    assert minimum(lst) == 1

def test_sum_positive(lst):
    assert sum_list(lst) == 15

```

## Extra Exercises

## C. Testing in Python

Consider this problem:

 > Given a list of integers, compute the average of only the *positive* elements.

There is a stub for a function that solves this problem in [rainfall.py](rainfall.py). Before implementing it, write some pytest compatible tests for the function.

* What needs to be tested for?
* What are the edge cases and how should they be handled?

Once the tests are written, commit them to git.

> See [here](solutions/rainfall.py)

## D. Python Programming

On a separate branch (`rainfall_solution`), implement the function such that it passes all the tests.

* How confident are you that your solution is correct?
* Is your solution very different from how you might do it in C?

Once you have done this, `git checkout master` and replace the `rainfall` stub with the following solution:

<details>
<summary>Don't look at this until after you've solved the problem with a list comprehension!</summary>

```python
def rainfall(integers):
    '''
    Single-loop solution
    '''
    total = 0
    count = 0
    for i in integers:
        if  i > 0:
            total += i
            count += 1
    if (count > 0):
        return total/count
    else:
        return None
```

</details>

It should pass all the tests you have written.

## E. Git Merges

Try to merge `rainfall_solution` back into `master`. This will create a merge conflict.

With the class, discuss which solution is better and how you might resolve the merge conflict to ensure it is the one used.
