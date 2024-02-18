# slicing = [start:stop:step]
# [0:5] = [:5]
# if slicing is [2:7] then we will stop at 7-1=6
num = [10,20,30,40,50,60,70,80,90]
print(num[1:-3:2])

data_list = ["Haddop","Python","Android","Java","Javascript","Ruby","C","C++","React"]


print(data_list[::-1]) #reversing list
print(data_list[-1])   #last
print(data_list[-2])   #second last
print(data_list[-3])   #third last
print(data_list[-3:])  #get last three element
print(data_list[1:-1]) #from index 1 to index -2
print(data_list[-3:9]) #from index -3 to index 8 
print(data_list[-5:-2]) #from index -5 to -3
print(data_list[1:-3:2]) #['Python', 'Java', 'Ruby']
print(data_list[1:5])
