# while loop  
count=0
while count<5:
    count += 1
    print(count)

x = 5
while (x != 12):
    print(x)
    x +=1

# for loop


for i in range(4):
    print(i)



for i in range(4):
    print("hello world")


mixed_data_list_var = [1, "apple", (2.5, 3.0), {"name": "Charlie"}, {1, 2, 3}]
for x in mixed_data_list_var:
    print(x)


for i in range(1,5):
    print(i)


# break statement

for i in range(1,11):
    if i == 9:
        break
    print(i)


# continue statement
for i in range(1,8):
    if (i==5):
        continue
    print(i)


# pass statement
for i in range(1,6):
    if(i==3):
        pass
    else:
        print(f"value of i is {i}.")




my_new_list=[(2,24),(3,34),(4,44),(5,55)]
for (t1,t2) in my_new_list:
    print(t2)


d= {
    'k1': 1,
    'k2': 2,
    'k3': 3
}
print(list(d.keys()))
print(list(d.values()))

for key in d:
    print(key)

for i,j in d.items():
    print(f"i is {i} and j is {j}")

for x in d.values():
    print(x)

count = 0
for i in 'abcde':
    print(f"at {count} index we value {i}.")
    count +=1

from random import shuffle
xyz_list = [10,20,30,40,50,60,70]
shuffle(xyz_list)
print(xyz_list)

from random import randint
k=randint(0,100)
print(k)

xyz_list = [10,20,30,40,50,60,70]
print(min(xyz_list))
print(max(xyz_list))



x = [x **2 for x in [x for x in range(0,11) if x%2 ==0]]
print(x)