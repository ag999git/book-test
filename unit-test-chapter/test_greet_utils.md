### 1. Solution to the following Problem
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
