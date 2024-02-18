# Instance Methods: These methods operate on instance variables and are the most common 
# type of method in Python classes. They take the instance itself (usually referred to as self) 
# as the first parameter.

# example 1
class MyClass:
    def __init__(self, x):
        self.x = x
    
    def print_value(self):
        print(self.x)

# Creating an instance of MyClass
obj = MyClass(5)
obj.print_value()  # Output: 5


# example 2
class MarksInAllSubjects:
    def __init__(self,math,physics,chemistry):
        self.math = math
        self.physics = physics
        self.chemistry = chemistry
    def get_mathmarks(self):
        return self.math
    def set_mathmarks(self,math_update):
        self.math=math_update
        return self.math
numbers = MarksInAllSubjects(90,100,60)
print(numbers.get_mathmarks())
print(numbers.set_mathmarks(80))


    
# Class Methods: These methods operate on class variables and are decorated with @classmethod. 
# They take the class itself (usually referred to as cls) as the first parameter.

# example 1
class MyClass:
    class_variable = 0
    
    @classmethod
    def increment_class_variable(cls):
        cls.class_variable += 1
    
    @classmethod
    def get_class_variable(cls):
        return cls.class_variable

# Calling class methods
MyClass.increment_class_variable()
print(MyClass.get_class_variable())  # Output: 1


# example 2

class Car:
    wheels = 4
    engine = 'echma'
    @classmethod
    def modifing_wheels_engien(cls,tire,engine):
        cls.wheels = tire
        cls.engine = engine
    @classmethod
    def get_wheels_engine(cls):
        print(f'this car has {cls.wheels} wheels and {cls.engine} engine.')

model1 = Car()
model1.get_wheels_engine()
model1.modifing_wheels_engien(8,'fedel')
model1.get_wheels_engine()


# example 3

class Car:
    wheels = 4
    engine = 'echma'
    @classmethod
    def modifing_wheels_engien(cls,tire,engine):
        cls.wheels = tire
        cls.engine = engine
    @classmethod
    def get_wheels_engine(cls):
        print(f'this car has {cls.wheels} wheels and {cls.engine} engine.')
    def x(self):
        print(f"this car has {self.wheels} wheels and {self.engine} engine.")
model1 = Car()
#model1.get_wheels_engine()
model1.modifing_wheels_engien(8,'fedel')
model1.get_wheels_engine()
Car.wheels = 12
Car.engine = 'turbo'
model1.x()


# Static Methods: These methods don't operate on instance or class variables. They are decorated 
# with @staticmethod and behave like regular functions, except they are defined within a class 
# for code organization purposes.


# example 1
class MathOperations:
    @staticmethod
    def add(x, y):
        return x + y
    
    @staticmethod
    def multiply(x, y):
        return x * y

# Calling static methods
print(MathOperations.add(2, 3))        # Output: 5
print(MathOperations.multiply(2, 3))   # Output: 6


# example 2

class Car: 
    wheels = 0
    def __init__(self,name,mile):
        self.name = name
        self.mile = mile
    @classmethod
    def get_wheels(cls,num):
        cls.wheels = num
        
    def carinfo(self):
        print(f"this is {self.name} , it gives {self.mile} miles per lt. and it has {self.wheels} tiers.")
        
    @staticmethod
    def sum(x,y):
        print("addition of x and y is", int(x)+int(y))
        
        
classic = Car("sydan",25)
classic.carinfo()
Car.sum(5,6)      
classic.sum(5,6)
Car.wheels = 4
classic.carinfo()
classic.get_wheels(12)
classic.carinfo()


    
        
    