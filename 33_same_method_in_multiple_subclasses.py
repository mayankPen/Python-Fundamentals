# example 1
class A:
    def show(self):
        print('I am part of A')
class B:
    def show(self):
        print('I am part of B')

class C(A,B):
    def __init__(self):
        print('I am inside C')

c = C()
c.show()
# output
# I am inside C
# I am part of A


# example - 2
class A:
    def show(self):
        print('I am part of A')
class B:
    def show(self):
        print('I am part of B')

class C(B,A):
    def __init__(self):
        print('I am inside C')

c = C()
c.show()

# output -
# I am inside C
# I am part of B

# example 3

class A:
    def show(self):
        print('Inside A')
class B(A):
    def show(self):
        print('Inside B')
b = B()
b.show()

# output - Inside B

