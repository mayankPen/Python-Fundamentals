# List -- list is a set of elements enclosed within square brackets.
# difference between list and tuple --
# 1. list is enclosed in square brackets and elements of tuple are enclosed within parenthesis.
# 2. tuple is faster then list.
# 3. list is mutable and tuple is immutable.


# Creating a list:
my_list = [1, 2, 3, 4, 5]

# adding element 
my_list = [1, 2, 3, 4, 5]
my_list[1] = "java" 
print(my_list)


# accessing elements
first_element = my_list[0]
second_element= my_list[1]

print(first_element, second_element)

# slicing elements
sublist = my_list[1:4]
print(sublist)

# Appending elements: - Adding an element to the end of the list
my_list.append(6)
print(my_list)


# Extending lists: - Extending the list by appending elements from another list
another_list=[7,8,9]
my_list.extend(another_list)
print(my_list)

# Inserting elements: - inserting elements at particular index
my_list.insert(2, 10)  
print(my_list)


# Removing elements: - removing first occurance of particular element
my_list.remove(2)
print(my_list)

# Popping elements: -- Remove and return the last element
popped_element = my_list.pop()
print(popped_element)

# Index of an element: - Get the index of the first occurrence of particular element
index_of_el= my_list.index(4)
print(index_of_el)

# Count occurrences: - counting occurance of particular element in list
my_list = [1, 2, 3, 4, 2, 5, 6, 2, 7]
count_el = my_list.count(2)
print(count_el)


# Reversing: -- Reverse the order of elements in the list
my_list = [1, 2, 3, 4, 5]
my_list.reverse()
print(my_list)

# Sorting: - Sort the list in ascending order
my_list=[5, 2, 8, 1, 3]
my_list.sort()
print(my_list)


# Copying: - Create a copy of the list
my_list=[5, 2, 8, 1, 3]
copy_my_li = my_list.copy()
print(copy_my_li)


# rmoving elements -  Remove all elements from the list
my_list=[5, 2, 8, 1, 3]
my_list.clear()
print(my_list)


#List comprehension:
my_list=[1,2,3,4]
x=[x**2 for x in [x+1 for x in my_list]]
print(x)

mixed_data_list_var = [1, "apple", (2.5, 3.0), {"name": "Charlie"}, {1, 2, 3}]
mixed_data_list_var[3]["name"] = "Mayank"
print(mixed_data_list_var)


data_list = ["Haddop","Python","Android"]
print(data_list*2)



y = []
x= [11,12,13,14]
for i in x:
    y.append(i**2)
print(y)