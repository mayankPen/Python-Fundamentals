# functions example in python - 1

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

def add(num1,num2):
    sum = num1+num2
    return sum
print(f"sum of {num1} and {num2} is : {add(num1,num2)}")


# functions example in python - 2

name = input("Enter your name : ")
number = int(input("Enter your age : "))

def data(number,name):
    print(f"you are {name} and your age is {number}.")

data(name,number)
