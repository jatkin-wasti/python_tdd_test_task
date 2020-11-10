## TDD Task
- Create a new Repo on github
- Create a new project in pycharm
- Name it tdd_test_task
- Create a file to write tests
- Create a file to write code
- Implement comments
- Create a README to document the steps to successfully achieve the task

- Create a test that checks  if a number has a remained of 0 when divided by a second number
- If True pass the test
- If False fail the test
- Create a class and method to write code to pass the test

- Create a test to check if the given values are positive
- Create a method in the class to pass the test
## Solution
### Creating the files and writing the test class
- First we create our test file which should be named test_(name_of_file_being_tested)
- Let's call our files ```checker.py``` and ```test_checker.py``` as the task wants us to check various conditions
- Importing our testing modules and the class we are testing
```
from checker import Checker
import unittest
import pytest
```
- It's okay if the ```from checker import Checker``` line is underlined red, we haven't created the Checker class yet 
so this is to be expected
- Now we'll make our testing class that will inherit from the unittest Testcase framework
```
class TestChecker(unittest.TestCase):
```
- We want to use this class to test the functionality of the Checker class, so we'll instantiate an object of the 
Checker class
- Again, if this is highlighted or underlined red don't worry. This is to be expected at this stage
```
    test = Checker()
```
- Now we'll right our tests for the Checker class methods. Let's name these ```clean_div``` and ```positive```
- Just like when naming our file, our testing methods should match these method names but start with ```test_```
```
    def test_clean_div(self):
        self.assertEqual(self.test.clean_div(10, 5), True)
        self.assertEqual(self.test.clean_div(10, 4), False)

    def test_positive(self):
        self.assertEqual(self.test.positive(-5), False)
        self.assertEqual(self.test.positive(8), True)
```
- In these methods we are checking the outputs of the Checker methods against the expected values i.e. 
We look to see if the clean_div method returns True when we try to divide 10 by 5 (which it should as 5 cleanly divides 
10 with no remainder)
- We also checks that the method returns False when it should, by checking its output when we divide 10 by 4
### Writing the class to be tested
- First we'll create the class with the name ```Checker``` as that's what we've used in our testing file
```
class Checker:
```
- Then we'll create our methods to test, again these need to match the names used in the testing file but without the 
"test_" prefix
- In these methods we will simply return true if the conditions are met and false if they are not
```
    def clean_div(self, val1, val2):
        if val1 % val2 == 0:
            return True  # If there is no remainder after dividing then we should return True
        else:
            return False  # Otherwise we should return false

    # Creating our positive method which checks if a number is positive or not
    def positive(self, val1):
        if val1 > 0:
            return True  # If it is positive then we should return True 
        else:
            return False  # If it is negative then we should return False

```
- Then we can run the file and see if any tests fail
- If they do, we can take a closer look using ```pytest -v```
- But all of the tests are successful so there is no need to do so in this instance