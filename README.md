# Object Oriented Programming
*Author: Jeet Soni*

*Date: 09/14/2023*

----

### **Description**
This exercise will always be in my 'memory' get it? 

Here we are, object orientated programming, the word itself sounds hard. I learned concepts of object oriented programming by solving some problem. It was hard for me to understand the benefits of them but when I started coding, I saw how important and useful they are. 

### **1. Create a Class**:
   **Create a class called `Person` with attributes `name` and `age`. Write a method `greet` that prints a greeting message with the person's name and age.**

I created a Person class using `class` keyword and in there I first defined the `__init__` and using keyword `self`, I initialized the attributes. After, I defined `greet()` method inside the class to greet the user. 

### **2. Inheritance**:
   **Create a class called `Student` that inherits from the `Person` class. Add an additional attribute `student_id` and a method `study` that prints a message indicating that the student is studying.**

I created the class called `Student` and then I passed in `Person` class I had already created in the Student class so it can inherit all Person class properties. I initialized the additional `student_id` attribute. Then, I created the study method to indicate the student records.

### **3. Encapsulation**:
   **Create a class called `BankAccount` with attributes `balance` and `account_holder`. Implement methods `deposit` and `withdraw` that modify the balance. Ensure that the `balance` attribute is private and can only be accessed or modified through these methods.**

I created a BankAccount class and initialized the balance and account holder attributes. I used `__balance` to make the balance attribute private. I created the `deposit()` and `withdraw()` methods to do the calculations. The balance attribute can only be accessed through these methods. 

### **4. Polymorphism**:
   **Create a class hierarchy involving animals. Have a base class `Animal` with a method `speak()`. Create subclasses like `Dog`, `Cat`, and `Cow`, each with their own `speak` method to represent the sound they make. Create instances of these classes and call their `speak` methods.**

First, created the base class Animal with method speak() that doesn't do anything. Then I created subclasses Dog, Cat and Cow each with their speak() method and what they speak. I created the instances of these classes and called their speak method.

### **5. Composition**:
   **Create a class called `Author` with attributes `name` and `books`. Create a class called `Book` with attributes `title`, `author`, and `publication_year`. Use composition to represent that an `Author` can have multiple `Book` instances.**

I created a class Author with attributes name and books and then I created a class with attributes title, author and publication year. I initialized all the attributes with `__init__` method. To show compostion and Author can have multiple book instances, I added instances of `Book` object in `Author` class.

### **6. Method Overloading**:
   **Implement method overloading in a class called `Calculator` to perform addition for 2 numbers, 3 numbers, and 4 numbers. The method should be named `add`.**

I created a class Calculator and defined add() method inside the class. I passed in 4 parameters in add method. I set each parameter to `None` and checked with if and else statements for how many values does user pass in and do the calculations according to that. `None` keyword sets the variable to default None. 

### 7. **Class Variables**:
   **Create a class `Car` with a class variable `total_cars` to keep track of the total number of cars created. Increment this variable every time a new car object is created.**

I created the class called Car with variable `total_cars` and set it equal to 0. I initialized the variable using the `__init__` method and inside that I incremented the `total_car` variable by 1 everytime a new car object was created. 

### 8. **Magic Methods**:
   **Implement the `__str__` and `__eq__` magic methods in a class called `Point` to represent 2D points. The `__str__` method should return a string representation of the point, and the `__eq__` method should compare two points for equality.**

First, I created a class called Point, inside that class I passed in 2 variables in the `__init__` method. I initialzed those attributes. Next, I created a `__str__` method to return he string representation of the points. To check for the equality of the 2 points, I created `__eq__` method with the `other` variable passed in the method to check for the equality of 2 objects. It will either return True or False. 

### 9. **Abstract Base Class**:
   **Use the `abc` module to create an abstract base class called `Shape` with an abstract method `area()`. Then create subclasses like `Circle` and `Rectangle` that implement the `area` method.**

I imported the abc module from ABC. I created the base class Shape and passed in `ABC` with abstract method area() with `pass` keyword inside the method. Then, I created subclasses Circle and Rectangle with inheritance of Shape class each with their own area methods. I passed in the formulas to calculate the area of Circle and Rectangle. The Shape() class won't be initialized because of `@abstractclassmethod`. 

---

Oh boy, I can't say this was easy but I learned a lot about the importance and benefits of Object Oriented programming. This exercise taught me how to implement classes and how to use them. 

Enjoy,

Jeet


















