class Outer:
    def show_outer(self):
        print('This is outer class definition.')
    class Inner:
        def show_inner(self):
            print('This is inner class definition')
        class InnerInner:
            def show_inner_inner(self,msg):
                print(f'This is inner class inside inner class with msg - {msg}')

outer = Outer()
inner = outer.Inner()
inner2 = inner.InnerInner()
inner2.show_inner_inner('<nested inner>')
