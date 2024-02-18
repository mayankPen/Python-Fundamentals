# multiple innerclasses

class Outer:
    def outershow(self,msg):
        print(f'This is outer class and it\'s message is {msg}')
    class InnerClass1:
        def inner1show(self,msg):
            print(f'This is inner1 class and it\'s message is {msg}')
    class InnerClass2:
        def inner2show(self,msg):
            print(f'This is inner2 class and it\'s message is {msg}')
            
outer = Outer()
inner1 = outer.InnerClass1()
inner2 = outer.InnerClass2()
outer.outershow('Outside mil')
inner1.inner1show('chal anndr')
inner2.inner2show('anndr mil')