# 'is' -- returs True if variables on either side of the operator have same
# value or otherwise False

# 'is not' -- return True if variables on either side of the operators are
# not having same value and return Flase otherwise

a=6
b=6
x=8
y=9
print(a is b)
print(x is y)
print(a is not b)
print(x is not y)


# 'in' - evaluates to true if it finds element in the specified sequence and false otherwise.
# 'not in' - evaluates to true if it do not find element in the specified sequence and false 
#  otherwise.


mixed_data_list_var = [1, "apple", (2.5, 3.0), {"name": "Charlie"}, {1, 2, 3}]
dictionary_var= {
    'name': 'John',
    'age': 25,
    'city': 'New York'
}

print("apple" in mixed_data_list_var)
print("age" not in dictionary_var)


# all() function returns true if all elements inside it are true.
# any() function returns true if any one element inside it is true.
# any() function returns false if all elements inside it are false.

a = [2,6,9,3]
b = [0,56,5,99]
c = [False, 0, None]
x=all(a)
y=all(b)
z=any(b)
q=any(c)


