Introduction to Git and Github

1. What is Git? Git is a version control system that lets you manage and keep track of your source code history. 
2. What is GitHub? GitHub is a cloud-based hosting service that lets you manage Git repositories.

A Computer Science Fundamental Concept:
Object-Oriented Programming (OOP):
In this guide, I will be delving into OOP basics using Python 3. Ready? Go!
We will cover : 
1. What is OOP in Python?
2. Defining a class in Python
3. Defining Instance methods in Python

1. What is OOP in Python?

Object-oriented programming (OOP) is a method of structuring a program by bundling related properties and behaviors into individual objects.

Conceptually, objects are like the components of a system. Think of a program as a factory assembly line of sorts. At each step of the assembly line a system component processes some material, ultimately transforming raw material into a finished product.

An object contains data, like the raw or preprocessed materials at each step on an assembly line, and behavior, like the action each assembly line component performs.

For instance, an object could represent a person with properties like a name, age, and address and behaviors such as walking, talking, breathing, and running. Or it could represent an email with properties like a recipient list, subject, and body and behaviors like adding attachments and sending.

Object-oriented programming is an approach for modeling concrete, real-world things, like cars, as well as relations between things, like companies and employees, students and teachers, and so on. OOP models real-world entities as software objects that have some data associated with them and can perform certain functions.




2. Defining a class in Python

Classes make code more manageable and maintainable as opposed to using lists to store objects.
A class is a blueprint for how something should be formed while an instance is an object that is built from a class and contains properties and data.

2a. How to define a class:
    class Car:
        pass
The Car class isn’t very interesting right now, so let’s spruce it up a bit by defining some properties that all Car objects should have. There are a number of properties that we can choose from, including color, model, and price. To keep things simple, we’ll just use color and model. 
    class Cars:
        def __init__(self, color, model):
            self.color = color #creates an attribute color and assigns it to the value of the color parameter
            self.model = model #creates an attribute model and assigns it to the value of the model parameter
The __init__ metod is called a dunder method (a special method in Python, check it out!). Color and model are known as instance attributes because they are created under the __init__ method.

2b. How to instantiate an object in Python.
Creating a new object from a class is called instantiating an object. You can instantiate a new Car object by typing the name of the class, followed by opening and closing parentheses:
    eg:
    tesla = Car('Red','ABX') #This instantiates a tesla object whose properties are that is red and that it is model ABX



3. Defining Instance Methods in Python

Instance methods are functions that are defined inside a class and can only be called from an instance of that class. Just like .__init__(), an instance method’s first parameter is always self.

Open a new editor window in IDLE and type in the following Car class:


This Car class has two instance methods:

.description() returns a string displaying the color and model of the car.


Save the modified Car class to a file called car.py and press F5 to run the program. Then open the interactive window and type the following to see your instance methods in action:
