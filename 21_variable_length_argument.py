# Note -- we can pass *args and **keyargs into same function, but *args
# have to appear before **keyargs.

# example -- 1

from functools import reduce
def add(*agrs):
    print(agrs)
    print(type(agrs))
    return reduce(lambda a,b:a+b,agrs)

print(add(1,2,3,4,5,6))


# example -- 2
def allkeysvalues(**keyargs):
    print(keyargs)
    print(type(keyargs))
    
allkeysvalues(name="mayank",age=29,skill='devops')


# example -- 3

def dictkey(**data):
    print(data)
    for key,value in data.items():
        print(f"{key} == {value}")
    
dictkey(name="mayank",age=29,skill='devops')