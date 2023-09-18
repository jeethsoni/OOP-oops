"""
creating a class
"""


class Person:
    """person class to store a person's information"""

    # defining the init method with variables
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # greet method that will print the message
    def greet(self):
        """greeting with user's name and age"""

        print(f"Hello, {self.name}, Welcome to the python world.")
        print(f"I see you are {self.age} years young.")
        print("you will forever be with us in our 'memory', get it? lol")
