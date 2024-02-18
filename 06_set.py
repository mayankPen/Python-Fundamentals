# In Python, sets are mutable and unordered collections of unique elements.
# set  do not support indexing or slicing like lists or tuples.


#Iterating over elements:

my_set={1, 2, 3, 4, 5}
for item in my_set:
    print(item)

#Converting set to a list:
my_set={1, 2, 3, 4, 5, 96}

new_set=list(my_set)

print(new_set[0],new_set[5])

print(type(new_set[3]))



# membership test:
print(5 in my_set)

if(4 in my_set):
    print('4 is a member of set')


my_set = {1, 2, 3}

#Adding Elements:
my_set.add(4)
print(my_set)

#Removing Elements:
# remove(): Removes the specified element from the set. 
# Raises an error if the element is not present.
my_set.remove(3)


# discard(): Removes the specified element from the set, but does not 
# raise an error if the element is not present.
my_set.discard(3)


# Combining Sets:
# union(): Returns a new set containing all unique elements from both sets.

set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1.union(set2)
print(union_set)
set1.update(set2)
print(set1)

# Intersection:
# intersection(): Returns a new set containing common elements 
# between two sets.

intersection_set = set1.intersection(set2)

#Difference:
#difference(): Returns a new set with elements from the first set 
#that are not in the second set.

set1 = {1, 2, 3}
set2 = {3, 4, 5}
difference_set = set1.difference(set2)
print(difference_set)



# issubset(): Returns True if one set is a subset of another.
# issuperset(): Returns True if one set is a superset of another.
A = {1, 2, 3}
B = {1, 2, 3, 4, 5}

is_subset = A.issubset(B)
is_superset = B.issuperset(A)

print(is_subset)
print(is_superset)


#copy(): Creates a shallow copy of the set.
#clear(): Removes all elements from the set.
#len(): Returns the number of elements in the set.

marks_set = {50,45,40,35}
dup_marks_set =marks_set.copy()
marks_set.clear()
print(marks_set)


marks_set = {50,45,40,35}
size = len(marks_set)