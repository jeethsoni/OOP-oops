"""
This python scipt is the main script to run all the classes
and print the result

@ usage python3 main.py
"""


from modules.animal import Dog, Cow
from modules.calculator import Calculator
from modules.car import Car
from modules.person import Person
from modules.student import Student
from modules.bank_account import BankAccount
from modules.point import Point
from modules.shapes import Rectangle, Circle


def main():

    # creating an instance of 'Person' and assigning it to user
    user = Person("Jeet", 20)
    # passing the values in greet function
    user.greet()

    # creating an instance of 'Student' class with values
    student_data = Student(22, "Jeet", 20)
    student_data.study()

    # creating an instance of 'Bank Account' class with values
    my_bank_account = BankAccount(900, "Jeet")
    print(f"You have withdrawn: $ {my_bank_account.withdraw(200)}")

    # creating an instance of 'Dog' class
    dog = Dog()
    print(dog.speak())

    # creating an instance of 'Cow' class
    cow = Cow()
    print(cow.speak())

    # creating an instance of 'Calculator" class
    my_calculator = Calculator()
    print(my_calculator.add(2, 3, 4, 5))  # performing addition with 4 values
    print(my_calculator.add(2, 3))  # performing addition with 2 values

    # created instance of 'Car' class
    my_car = Car()  # noqa
    honda = Car()
    print(f"total car instances: {honda.total_cars}")

    # creating two instances of 'Point' class
    coordinates = Point(2, 2)
    my_point = Point(2, 3)
    print(coordinates)  # string representation of points
    print(my_point == coordinates)  # checking for equality of 2 points

    # creating an instance of 'Rectangle' class
    rec = Rectangle(2, 3)
    print(rec.area())  # area of rectangle

    # creating an instance of 'Circle' class
    my_circle = Circle(2)
    print(my_circle.area())  # area of circle


if __name__ == "__main__":
    main()
