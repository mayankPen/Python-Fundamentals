

# Question -- what is a class?
# Answer -- class is a description of object's property set and set of operations. we can also
# say that class is a blueprint of an object.

# Question -- what is object?
# Answer -- An object is an instance of the class.

# example -- 1

class Computer:
    def config(self):
        print("i9,16gb,2Tb")

comp1 = Computer()
Computer.config(comp1)
comp1.config()

# example -- 2

class Computer:
    def config(self,name):
        print('i5,16gb,1Tb',name)
comp1 = Computer()
comp2 = Computer()
Computer.config(comp1,'something')
comp1.config('terrible')
comp2.config('happened')

