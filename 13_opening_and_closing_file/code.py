# reading file with -- "r"
# file pointer is at the begining of the file.
# file has to be there before
# overwriting happens
try:
    my_file=open("mayank.txt","r")
finally:
    print(my_file.read())
    my_file.close()

# cat mayank.txt

# reading and writing file with -- "r+"
# file has to be there before
# file pointer is at the begining of the file.
# overwriting happens
  
try:
    my_file=open("mayank.txt","r+")
    my_file.write("I am Dinesh")
finally:
    my_file.close()

# cat mayank.txt



# opening file for writing only with - "w"
# if file does not exist then file will be created.
# previously written content will be removed 
# overwriting does not happen 
# whatever in the double quotes will be written in the file.
    

try:
    my_file = open("mayank.txt","w")
    my_file.write("I am new king and I will rule now.")
finally:
    my_file.close()

# cat mayank.txt
    

# opening file for writing and reading with - "w+"
# if file does not exist then file will be created.
# previously written content will be removed 
# overwriting does not happen 
# whatever in the double quotes will be written in the file.
    

try:
    x_file = open("mayank.txt","w+")
    x_file.write("Soon I will be in Delhi , I do'nt want to waste life.")
finally:
    x_file.close()

# cat mayank.txt


# opening file for appending with -- "a"
# pointer is at the end of file, so file opens in appending mode.
# if file does not exit then it create new file .
    
try:
    y_file = open("mayank.txt","a")
    y_file.write("There are lot of it companies in pune.")
finally:
    y_file.close()

# cat mayank.txt


# opening file for both appending and reading with -- "a+"
# pointer is at the end of file, so file opens in appending mode.
# if file does not exit then it create new file .


try:
    z_file = open("mayank.txt","a+")
    z_file.write("appending again go....")
finally:
    z_file.close()


# cat mayank.txt


# reading file in different location in windows

try:
    my_file = open("C:\\Users\\This-Pc\\Videos\\logxyz.txt","r")
    print(my_file.read())
finally:
    my_file.close()