#--------OOPs
'''
>Object-Oriented Programming (OOPs) is a programming paradigm in Python that organizes code around objects and classes rather than functions and logic. 
>This approach binds data (attributes) and behavior (methods) into a single unit. 
>OOPs makes code modular, highly reusable, and scalable for complex software applications.

'''
#-----Class
'''
>A class is a collection of objects.
>Classes are blueprints for creating objects.
 >A class defines a set of attributes and methods that the created objects (instances) can have.  
>Classes are created by keyword class.
>Attributes are the variables that belong to a class.
>Attributes are always public and can be accessed using the dot (.) operator. Example: Myclass.Myattribute
'''
#----Object
'''
>An Object is an instance of a Class. It represents a specific implementation of the class and holds its own data. An object consists of:
>State: represented by the attributes and reflects the properties of an object.
>Behavior: represented by the methods of an object and reflects the response of an object to other objects.
>Identity: gives a unique name to an object and enables one object to interact with other objects.

'''
'''
Class

A blueprint/template for creating objects. No memory is allocated for it until an object is actually created.

python
class Student:
    college = "SRTM"  # class attribute

    def __init__(self, name, marks):
        self.name = name      # instance attribute
        self.marks = marks
Object

An actual instance of a class — created when you "run" the class with real data.

python
s1 = Student("Ravi", 84)   # s1 is an object
__new__

The method that actually creates the object (allocates memory) — it runs first, before __init__. It's technically a static method that returns a new instance.

python
class Student:
    def __new__(cls, *args, **kwargs):
        print("Creating object...")
        return super().__new__(cls)

    def __init__(self, name):
        print("Initializing object...")
        self.name = name

Order: __new__ → object created → __init__ → attributes set.

__init__

The constructor that initializes the object right after it's created — sets up attributes. It doesn't allocate memory, just assigns values to an already-existing object.

self

Refers to the current instance. It's the first parameter of instance methods, letting you access that specific object's attributes/methods inside the class.

python
def show(self):
    print(self.name)   # 'self' = the object it's called on
cls

Refers to the current class (not the instance). Used in classmethods — when the logic is class-level, not tied to any one object.

python
class Student:
    count = 0

    @classmethod
    def increment(cls):
        cls.count += 1
Quick interview-trap comparison table:
Concept	Refers to	When called
self	instance	in instance methods
cls	class	in classmethods
__new__	object creation	first (allocates memory)
__init__	object initialization	after (sets values)



'''

# class student:
#     pass

# class employee:
#     passno

# ravi=student()
# om=employee()

# # print(type(ravi))
# # print(type(om))

# print(dir(student))
# print(dir(employee))



#interview question
#ehat is attribute and method
#types of attribute
