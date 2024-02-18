# Note -- __init__ is called automatically for each object
# Note -- whatever is inside __init__ is executed as soon as object is created,look exmple 3


# example 1

class Computer:
    def __init__(self):
        print('inside init')

comp1 = Computer()
comp2 = Computer()


# output  - 
# inside init
# inside init

# example 2

class Computer:
    def __init__(self,name):
        print('inside init',name)

comp1 = Computer('Mayank')
comp2 = Computer('Anuj')


# output --     
# inside init Mayank
# inside init Anuj


# example 3

class Computer:
    def __init__(self,obj):
        print('inside init',obj)
    def config(self,x):
        print('i5,16gb,1Tb',x)
comp1 = Computer('comp1')
comp2 = Computer('comp2')
comp1.config('something')
comp2.config('done')

# output -     
# inside init comp1
# inside init comp2
# i5,16gb,1Tb something
# i5,16gb,1Tb done


# example 3

class Parent:
    def __init__(self,x):
        print(f"I am inside Parent init with {x}")
    def average(self,a,b):
        return (a+b)/2
class Parent2:
    def __init__(self,y):
        print(f"I am inside Parent2 init with {y}")
class Child(Parent,Parent2):
    def __init__(self):
        print(f'I am inside Child init with nobudy.')
        Parent.__init__(self,'kartik')
        Parent2.__init__(self,'anuj')
        print(f'average is {Parent.average(self,5,4)}')
ch = Child()