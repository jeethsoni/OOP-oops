class Calculator:
    """calculator class to do add calculations"""

    # initializing the attribute
    def __init__(self):
        print("Calculator created")

    # add method to add the user passed numbers and perform calculations
    def add(self, a=None, b=None, c=None, d=None):
        """adding the numbers depending on the amount of values passed in"""

        if ((a is not None) and (b is not None) and (c is not None) and (d is not None)):  # if 4 values passed in do this  # noqa
            sum = a+b+c+d
        elif ((a is not None) and (b is not None) and (c is not None)):  # if 3 values passed in  # noqa
            sum = a+b+c
        elif ((a is not None) and (b is not None)):  # if 2 values passed in
            sum = a+b
        else:
            sum = a

        return sum  # return the total sum
