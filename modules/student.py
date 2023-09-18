"""
inheritance
"""

from modules.person import Person


class Student(Person):
    """student class that inherits from Person class"""

    # initialzing Person class attributes with additional attribute
    def __init__(self, student_id, name, age):
        Person.__init__(self, name, age)
        self.student_id = student_id

    def study(self):
        """study method to check where the student is studying"""

        print(f"student id: {self.student_id}, name: {self.name}, age: {self.age}")  # noqa
        print("This student is studying at Rutgers University")
