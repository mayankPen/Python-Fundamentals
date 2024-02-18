# normal string formatting 
name='mayank'
age=60
print('I am '+name+'. I am '+str(age)+' year\'s old.')
#-------------------------------------------------------------

# string formatting using ---- .format()

print("I am {} years old.".format('fifty'))
age=30
print('I am {} yeas old.'.format(age))
print('I have got {} rupees in my pocket.'.format(500))

a, b, c = 5, 6, 7
print('a, b, and c in increasing order {}, {}, {}'.format(a, b, c))
print('a, b, and c in decreasing order {}, {}, {}'.format(c, b, a))
print('a, b, and c in random order {}, {}, {}'.format(b, a, c))

print('I am {} and I socred {:.2f} out of {} in exam'.format('mayank',12.3639,50))
#----------------------------------------------------------------


# string formatting with 'f'

player = 'virat kholi'
runs,year = 765,2023
print(f"{player} scored {runs} runs in {year} world cup !")

name = 'Anuj'
gotmarks = 12.369852147
totalmarks = 50
print(f"He is {name} and he has got {gotmarks:.2f} out of {totalmarks}.")
#-----------------------------------------------------------------

# string formatting with %s

print('%s and %s are brothers.'%('Mayank','Anuj'))

print("I am %s and I have got %.2f marks out of %s."%("mayank",12.6985214,50))

print('Floating point number is %.2f.'%(13.144))



x = 2.36985
print(f"value of x is {x:.2f}")