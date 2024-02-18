# example 1
class A:
    def __init__(self):
        print('inside init of A')
    def feature1(self):
        print('This is feature one.')
    def feature2(self):
        print('This is feature two')
class B(A):
    def __init__(self):
        print('inside init of B')
    def feature3(self):
        print('This is a feature three.')
    def feature4(self):
        print('This is a feature four.')

b = B()

# example 2
class A:
    def __init__(self):
        print('inside init of A')
    def feature1(self):
        print('This is feature one.')
    def feature2(self):
        print('This is feature two')
class B(A):
    def __init__(self):
        print('inside init of B')
        super().__init__()   # here we are calling init of class A
    def feature3(self):
        print('This is a feature three.')
    def feature4(self):
        print('This is a feature four.')

b = B()

# If you create object of subclass , it will first try to find __init__ of subclass while 
# executing code. If it is not found then it will call __init__ of super class.

# example 3
class A:
    def __init__(self):
        print('inside init of A')
    def feature1(self):
        print('This is feature one.')
    def feature2(self):
        print('This is feature two')
class B(A):
    def feature3(self):
        print('This is a feature three.')
    def feature4(self):
        print('This is a feature four.')

b = B() 
# output -- inside init of A 

# example 4
class A:
    def __init__(self):
        print('inside init of A')
    def feature1(self):
        print('This is feature one.')
    def feature2(self):
        print('This is feature two')
class B:
    def __init__(self):
        print('inside init of B')
    def feature3(self):
        print('This is a feature three.')
    def feature4(self):
        print('This is a feature four.')
class C(A,B):
    def __init__(self):
        print('inside init of C')
        super().__init__()
c = C()

# example 5
class A:
    def __init__(self):
        print('inside init of A')
    def feature1(self):
        print('This is feature one.')
    def feature2(self):
        print('This is feature two')
class B:
    def __init__(self):
        print('inside init of B')
    def feature3(self):
        print('This is a feature three.')
    def feature4(self):
        print('This is a feature four.')
class C(B,A):
    def __init__(self):
        print('inside init of C')
        super().__init__()
c = C()

# example 6

class A:
    def show(self):
        print('I am In A')
class B(A):
    def show(self):
        print('I am In B')
        super().show()
b = B()
b.show()

