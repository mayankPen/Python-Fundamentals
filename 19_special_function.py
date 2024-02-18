# map() function -- syntax - map(function,iterable)
# the map function executes a specified function for each item in a iterable. The item is 
# sent to the function as a parameter returns an iterable.

def addition(a):
    return a+a

number=[1,2,3,4,5]
dubled = map(addition,number)
print(type(dubled))
print(dubled)
print(list(dubled))

def addall(a,b):
    return a+b

result = list(map(addall,(5,6,7),(8,9,10)))
print(result)



f = lambda a:a*a
list_x =[10,20,30,40,50]
sum = map(f,list_x)
print(list(sum))



list_o = list(range(-5,5))
print(list_o)


# filter() function -- The filter method filters the given sequence with the help of a function.
# function test each element in the sequence to be true or not.

# syntax -- filter(function,sequence)
result = list(filter(lambda x: x>0,range(-5,5)))
print(result)   # output --- [1, 2, 3, 4]


# checking even numbers without using lambda function
def check_even(num):
    return num%2 == 0
    
seq = list(range(0,21))

even_numbers = list(filter(check_even,seq))
print(even_numbers)  #output -- [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]


# another example related to age -- filtering ages - [5,12,17,22,18,36,7,12,55,14,96]

def check_age(age):
    if age >= 18:
        return True
    if age < 18:
        return False
        
ages = [5,12,17,22,18,36,7,12,55,14,28,96]

voters = list(filter(check_age,ages))
print(voters)


# reduce() function -- The reduce function is part of the 'functools' module in Python , it is 
# used to apply a specified function to the items of an iterable , when we want to reduce 
# iterable to a single accumulated result.

# calculate sum of element of [20, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20] using reduce function

from functools import reduce
list_num = [20, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
result = reduce(lambda a,b:a+b,list_num)
print(result)

#without lambda
from functools import reduce
def addall(a,b):
    return a+b
list_num = [20, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
result = reduce(addall,list_num)
print(result)



