# tuples-- Tuples can be accessed but can not be mutated but if
# we have list or dictionary as an elements of tuple then we can 
# mutate tuple.
# ex --   my_tuple = (2,"mayank",{"name":"anuj"},(2,99,3),[121,"xyz",87])

x=([50,65,60],{"name":"Mayank"})
x[0][1]=55
x[1]["name"]="Kartik"
print(x)




my_tuple = (1, 2, 3)

#Access Elements:
print(my_tuple[0]) 



#Slice a Tuple:
sub_tuple = my_tuple[1:3]  
print(sub_tuple)



#Concatenate Tuples:
new_tuple = my_tuple + (4, 5)
print(new_tuple)



#Check Membership:
print(2 in my_tuple)


#Find Length:
length = len(my_tuple)
print(length)



#Iterate Through a Tuple:
for item in my_tuple:
    print(item)



#Unpack Tuples:
a, b, c = my_tuple
print(a,b,c)



#Count Occurrences:
count_2 = my_tuple.count(2)
print(count_2)



#Find Index of an Element:
index_3 = my_tuple.index(3)
print(index_3)


#Convert to Tuple:
converted_tuple = tuple([1, 2, 3])
print(converted_tuple)





