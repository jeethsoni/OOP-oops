"""
Class variables
"""


class Car:
    """car class to store car informatiom"""

    total_cars = 0  # class variable

    def __init__(self):
        print("car added")

        # incrementing the variable as new car object is created
        Car.total_cars += 1
