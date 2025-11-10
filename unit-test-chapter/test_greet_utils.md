# Solution to the following 
# Greeting Function (with a subtle bug, a hidden logic mistake). 
# In the book the following problem was given:- The problem is is triple Quotes below

""" PROBLEM STARTS HERE
# greet_utils.py

# Bug:- an empty string "" or a None value?
def make_greeting(name):
    # BUG: forgets to handle empty or None names
    return "Hello, " + name + "!"
""" PROBLEM ENDS HERE
# The project was to create a unit test for the above problem

# SOLUTION STARTS HERE

# SOLUTION
# test_temperature_utils.py
import unittest
import temperature_utils

class TestTemperatureConversion(unittest.TestCase):
    def test_celsius_to_fahrenheit(self):
        result = temperature_utils.celsius_to_fahrenheit(100)
        self.assertEqual(result, 212)  # 100°C should be 212°F

unittest.main()

# SOLUTION ENDS HERE
