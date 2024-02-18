class Computer:
    def __init__(self):
        self.name = "mayank"
        self.age = 25
comp1 = Computer()

print(comp1.name)
print(comp1.age)

# setting value of property from outside
class Computer:
    def __init__(self):
        self.name = "Mayank"
        self.age = 29
comp1 = Computer()
comp2 = Computer()
comp1.name = "Anuj"
print(comp1.name)
print(comp2.name)

# output-    
# Anuj
# Mayank


# passing value of one object to another object or calling one object to another object.

class Computer:
    def __init__(self):
        self.name = "mayank"
        self.age = 25
    def updateage(self):
        self.age = 28
    def compare(self,other):
        if self.age == other.age:
            return True
        else:
            return False
comp1 = Computer()
comp2 = Computer()
if comp1.compare(comp2):
    print('Both are same age.')
if comp2.compare(comp1):
    print('Both are same age.')
comp2.updateage()
if comp1.compare(comp2):
    print('Both are same age.')
else:
    print('Both are different')
if comp2.compare(comp1):
    print('Both are same age.')
else:
    print('Both are different')
