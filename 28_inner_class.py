# example 1
class InfoApp:
    def __init__(self,name,age,rollN):
        self.name = name
        self.age = age
        self.rollN = rollN
        self.lap = self.Laptop()
    class Laptop:
        def __init__(self):
            self.cpu = 4
            self.ram = "8gb"
            self.space = '1TB'
            
info = InfoApp('Mayank',25,10005)
print(info.lap.space)

# Note -- you can access the inner class in outer class using self keyword, but we can not 
# access outer class in an inner class.

# example 2
class MyData:
    def __init__(self,name,rollnumber,age,cpu,ram,space):
        self.name = name
        self.age = age
        self.rollnumber = rollnumber
        self.lap = self.Laptop(cpu,ram,space)
    class Laptop:
        def __init__(self,cpu,ram,space):
            self.cpu = cpu
            self.ram = ram
            self.space = space
data = MyData('mayank',1005,29,20,'16gb','1TB')
print(data.lap.ram)

# example 3
class MyInfo:
    def __init__(self,name,rollno):
        self.name = name
        self.rollno = rollno
        self.lap = self.Laptop()
    def show(self):
        print(f"I am {self.name} and my roll number is {self.rollno}.")
        self.lap.show()
    class Laptop:
        def __init__(self):
            self.cpu = 4
            self.ram = '16gb'
            self.space = '500gb'
        def show(self):
            print(f'this computer has {self.cpu} ram {self.ram}, cpu and {self.space} space.')
            
data = MyInfo('Mayank',1005)
data.show()

# example 4
class Outer:
    def __init__(self):
        self.inner = self.Inner()
    def showouter(self,msg):
        self.inner.showinner(msg)
    class Inner:
        def showinner(self,msg):
            print(f'Message you passed is - {msg}')
out = Outer()
out.showouter('Great!@!#')

# example 5
class Outer:
    def __init__(self):
        self.inner = self.Inner()
    def outershow(self,msg):
        self.inner.innershow(msg)
    class Inner:
        def innershow(self,msg):
            print(f"Your message is -- {msg}")
Outer().Inner().innershow('@# hello @# hi $')


# In this example we created object of inner class inside outer class.
# what we can do is we can create object of inner class outside of outer class.

# example 1

class MyInfo:
    def __init__(self,name,rollno):
        self.name = name
        self.rollno = rollno
    class Laptop:
        def __init__(self,cpu,ram,space):
            self.cpu = cpu
            self.ram = ram
            self.space = space

data = MyInfo('Mayank',15)
lap = data.Laptop(20,'16gb','500GB')
print(lap.cpu)
print(lap.ram)
print(lap.space)

# example 2 

class Outer:
    class Inner:
        def innershow(self,msg):
            print(f"message from you is {msg}")
out = Outer()
inn = out.Inner()
inn.innershow('^^00^^LL$$')

# example 3
class Outer:
    class Inner:
        def innershow(self,msg):
            print(f"message from you is {msg}")

inn = Outer().Inner()
inn.innershow('LOL')

# example 4
class Outer:
    class Inner:
        def __init__(self,name,age):
            self.name = name
            self.age = age
        def show_inner_msg(self,msg):
            print(msg)
            print(f"your name is {self.name} and your age is {self.age}.")

outer = Outer()
inner = outer.Inner('Mayank',29)
inner.show_inner_msg('GoForIt')

