# example 1
class Salary:
    def __init__(self,pay,bonus):
        self.__pay = pay
        self.__bonus = bonus
    def total_pay(self):
        return ((self.__pay*12)+self.__bonus)
class Mydata:
    def __init__(self,name,age,pay,bonus):
        self.__name = name
        self.__age = age
        self.__mySalaryObj = Salary(pay,bonus)
    def gross_pay(self):
        print(self.__mySalaryObj.total_pay())
data = Mydata('Mayank',29,30000,15000)
data.gross_pay()

# example 2

class Salary:
    def __init__(self,pay,bonus):
        self.__pay= pay
        self.__bonus = bonus
    def total_salary(self):
        return ((self.__pay*12)+self.__bonus)
class Mydata:
    def __init__(self,name,age,grpay):
        self.__name = name
        self.__age = age
        self.__grpay = grpay
    def gross_pay(self):
        print(self.__grpay.total_salary())
salary = Salary(50000,15000)
data = Mydata('Mayank',30,salary)
data.gross_pay()
