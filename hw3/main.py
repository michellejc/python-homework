"""
This is the code that replit executes when you click the run button.

It prints each test result to evaluate which functions are correctly finished.

Feel free to add, delete, or modify the code in this file. It is just for you, it will not graded.
"""

# Import the actual functions so they are in the namespace
from homework_3_code import *

# Run & print all tests

from test_hello import test_hello # This is a sample. Not graded.
print(test_hello())

from test_is_strictly_increasing import test_is_strictly_increasing
print(test_is_strictly_increasing())

from test_is_all_equal import test_is_all_equal
print(test_is_all_equal())

from test_uniques import test_uniques
print(test_uniques())

from test_find_missing_item import test_find_missing_item
print(test_find_missing_item())

from test_is_valid import test_is_valid
print(test_is_valid())


print("tests pass for all functions 🙂") 

