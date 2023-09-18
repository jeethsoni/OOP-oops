from abc import ABC, abstractclassmethod


class Shape(ABC):
    """abstract method shape"""

    @abstractclassmethod
    def __init__(self, num1=None, num2=None):
        self.num1 = num1
        self.num2 = num2

    @abstractclassmethod
    def area(self):
        """abstract method area"""
        pass


class Rectangle(Shape):
    """subclass rectangle that inherits Shape class"""

    # initalizing the attributes from base class 'Shape'
    def __init__(self, num1, num2):
        super().__init__(num1, num2)

    def area(self):
        """area method to calculate area of rectangle"""
        return self.num1 * self.num2


class Circle(Shape):
    """subclass Circle inherits from Shape class"""

    # initalizing the attributes from base class 'Shape'
    def __init__(self, num1):
        super().__init__(num1)

    def area(self):
        """area method that calculates area of circle"""
        return 3.14 * self.num1 * self.num1
