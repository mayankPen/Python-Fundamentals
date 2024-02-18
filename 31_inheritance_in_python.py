# if class C inherit form class A and class B and at same time class B don't inherit from class A
# the we write class C as -- class C(A,B)

# if class C inherit form class A and class B and at same time class B also inherit from class A
# the we write all classes as -- class A , classB(A) and class C(B)
# example 1
class A:
    def feature1(self):
        print('This is feature one')
    def feature2(self):
        print('This is feature two')
class B(A):
    def feature3(self):
        print('This is feature three.')
    def feature4(self):
        print('This is feature four.')
class C(B):
    def feature5(self):
        print('This is feature five.')
    def feature6(self):
        print('This is feature six')
c = C()

# example 2
class A:
    def feature1(self):
        print('This is feature one')
    def feature2(self):
        print('This is feature two')
class B:
    def feature3(self):
        print('This is feature three.')
    def feature4(self):
        print('This is feature four.')
class C(A,B):
    def feature5(self):
        print('This is feature five.')
    def feature6(self):
        print('This is feature six')
a = A()
b = B()
c = C()
