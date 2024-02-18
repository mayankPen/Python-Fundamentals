name = input("enter name : ")
print(type(name))
age = input("enter age : ")
print(type(age))
print(f"I am {name} and I am {age} years old.")


######################################################
# creating the code for getting factorial of number.

number = input("Enter the number you want factorial of : ")
number = int(number)

if (number == 0 or number == 1):
    print(f"factorial of !{number} is : 1")
else:
    x=1
    for i in range(1,number+1):
        x = x*i
    print(f"factorial of !{number} is : {x}")
