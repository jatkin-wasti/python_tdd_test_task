# Creating our Checker class to hold the functionality we want to test
class Checker:
    # Creating our clean division method which checks if one value is cleanly divisible by the other
    def clean_div(self, val1, val2):
        if val1 % val2 == 0:
            return True  # If there is no remainder after dividing then we should return True
        else:
            return False  # Otherwise we should return false

    # Creating our positive method which checks if a number is positive or not
    def positive(self, val1):
        if val1 > 0:
            return True
        else:
            return False
