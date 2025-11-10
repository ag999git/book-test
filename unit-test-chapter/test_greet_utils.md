### 1. Give Solution to the following Problem
* Greeting Function (with a subtle bug, a hidden logic mistake). 
* In the book the following problem of the following buggy code to be unit tested was given:-


```python

# greet_utils.py

# Bug:- an empty string "" or a None value?
def make_greeting(name):
    # BUG: forgets to handle empty or None names
    return "Hello, " + name + "!"

```

### The solution unit test for tracing out the bug in above code is as follows:-

```python

# test_greet_utils.py

import unittest
import greet_utils

class TestGreeting(unittest.TestCase):

    def test_normal_name(self):
        result = greet_utils.make_greeting("Anita")
        self.assertEqual(result, "Hello, Anita!")

    def test_empty_name(self):
        # Empty name should produce a polite default greeting
        result = greet_utils.make_greeting("")
        self.assertEqual(result, "Hello there!")

    def test_none_name(self):
        # None should also not crash; should use default greeting
        result = greet_utils.make_greeting(None)
        self.assertEqual(result, "Hello there!")

unittest.main()

```

#### The corrected code is as follows:-
* It works because it takes care of "edge" cases like empty string ("") and None 

```python

def make_greeting(name):
    if not name:  # Handles "", None, etc.
        return "Hello there!"
    return "Hello, " + name + "!"

```






#### Note:-  `greet_utils.py` and `test_greet_utils.py` should be in same project directory



### 2. Give Solution to the following problem:-
* Bug:- Works fine for [2, 4, 6], etc. But what if the list is empty []?
* Then len(numbers) is 0, and you get a ZeroDivisionError — a common mistake humans forget to handle.

```python

# math_utils.py
# Bug:- Division by 0 if list is empty ie []

def average(numbers):
    total = sum(numbers)
    return total / len(numbers)

```

### The solution unit test for tracing out the bug in above code is as follows (Put solution in file:- `test_math_utils.py`):-

```python

# test_math_utils.py

import unittest
import math_utils

class TestAverageFunction(unittest.TestCase):

    def test_normal_list(self):
        result = math_utils.average([10, 20, 30])
        self.assertEqual(result, 20)

    def test_empty_list(self):
        # Empty list should not crash — should return 0 or None
        result = math_utils.average([])
        self.assertEqual(result, 0)

unittest.main()

```


#### The corrected code in file `math_utils.py` is as follows:-

```python

# math_utils.py

def average(numbers):
    if not numbers:        # Handles empty list safely
        return 0
    total = sum(numbers)
    return total / len(numbers)



```









