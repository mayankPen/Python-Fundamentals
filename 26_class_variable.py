
# variables which are used outside of class can be used anywhere in the
# program.
a = 50
class Car:
    def show(self):
        b = 50
        print(a+b)
car = Car()
car.show()

# Note -- we can set class variable (ex wheel) inside class like in given example.
# Note -- we set class variable using class name. (outside of class)
# Note -- we can access class variable using self keyword (inside of class)
# Note -- we can access class variable using object name (outside of class)


class Car:
    wheel = 4
    def __init__(self,name,mile):
        self.name = name
        self.mile = mile
    def cardata(self):
        print(f"this is {self.name} and it give {self.mile} mile per liter and it has {self.wheel} wheels.")
car1 = Car('BMW',85)
car2 = Car('FoxTruck',100)
car1.cardata()
print(car1.name,car1.mile,car1.wheel)
Car.wheel = 8
car2.cardata()
print(car2.name,car2.mile,car2.wheel)

# example 2
class Car:
    wheels = 4
    def __init__(self,name,model,engine):
        self.name = name
        self.model = model
        self.engine = engine
    def config(self):
        print(f'this is {self.name} it\'s model is {self.model} and engine is {self.engine} and has {self.wheels} wheels')
        # print(f'this is {self.name} it\'s model is {self.model} and engine is {self.engine} and has {wheels} wheels')  # wrong call of wheel
        
prod = Car('maruti',800,'m4')
prod2 = Car('suv','200','t50')
print(prod.wheels)
prod.config()
Car.wheels = 16
print(prod.wheels)
prod2.config()
