class Computer:
    def __init__(self,cpu,ram,space):
        self.cpu = cpu
        self.ram = ram
        self.space = space
    def config(self,number):
        print(f"this is {self.cpu} {self.ram} {self.space} and this is number {number}")

comp1 = Computer('i5','16gb','1Tb')
comp2 = Computer('i9','32gb','2Tb')
comp1.config(1)
comp2.config(2)

# output -  
# this is i5 16gb 1Tb and this is number 1
# this is i9 32gb 2Tb and this is number 2