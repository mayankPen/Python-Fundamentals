# in python lambda function or anonymus function means that a function without a name.

# you can have n number of arguments but it should be only of one expression.


f = lambda a: a*a
number = int(input("Enter number you want square of : "))
print(f"square of the {number} is : {f(number)}.")




square = lambda a:a*a
num = float(input("Enter number : "))
print(f"square of {num} is {square(num):.2f}")




a=int(input("Enter number a : "))
b=int(input("Enter number b : "))

f = lambda a,b: a+b

print(f"addition of {a} and {b} is : {f(a,b)}.")