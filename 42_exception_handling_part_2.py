# example 1
try:
    a = 10/0
except ZeroDivisionError:
    print('0 is divide mat kar chutiye')
    
# example 2
    
try:
    a = 10/0
except ZeroDivisionError:
    pass


# example 3
try:
    a = int(input('Enter the interger:'))
except ValueError:
    print('interger dal chutiye')

# example 4

# Define custom exception class
class NegativeNumberError(Exception):
    pass

try:
    a = int(input('Enter the number you want to get factorial of: '))
    if a < 0:
        raise NegativeNumberError('You have entered a negative number...')
except NegativeNumberError as e:
    print(f'{e}')


# example 5 
try:
    a = int(input('Enter the interger:'))
except ValueError as e:
    print(f'interger dal chutiye - {e}')

# output - 
# Enter the interger:"abc"
# interger dal chutiye - invalid literal for int() with base 10: '"abc"'