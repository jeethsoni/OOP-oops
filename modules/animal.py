# animal superclass
class Animal:
    """This is Animal base class"""

    def __init__(self):
        """initializes the aninal class"""
        print("I am an animal")

    def speak(self):
        pass


# subclasses
# dog class
class Dog(Animal):
    """Dog class inherits the properites of Animal class"""

    def __init__(self):
        """initalizes the Dog class"""
        Animal.__init__(self)

    def speak(self):
        """overides speak method in animal and defines it own speak method"""
        return "Dog says Woof"


# cat class
class Cat(Animal):
    """Cat class inherits the properites of Animal class"""

    def __init__(self):
        """initalizes the Cat class"""
        Animal.__init__(self)

    def speak(self):
        """overides speak method in animal and defines it own speak method"""
        return "Cat says Meow"


# cow class
class Cow(Animal):
    """Cow class inherits the properites of Animal class"""

    def __init__(self):
        """initalizes the Cow class"""
        Animal.__init__(self)

    def speak(self):
        """overides speak method in animal and defines it own speak method"""
        return "Cow says Moo"
