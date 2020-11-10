
class Checker:

    def clean_div(self, val1, val2):
        if val1 % val2 == 0:
            return True
        else:
            return False

    def positive(self, val1):
        if val1 > 0:
            return True
        else:
            return False
