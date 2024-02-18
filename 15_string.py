string = "edurekaeur"
print(string.capitalize())
print(string.count('e',0,len(string)))
print(string.count('ur',0,len(string)))
print(string.replace('e','&',3))
print(string.replace('ur','^',2))
print(string.upper())
print(string.index('e'))
print(string.index('k'))
print(string.index('ur'))

# return index at which the given letter is present in string.
# if given letter is not found then find will return -1 .
print(string.find('k'))  
