import os

# Check if a file exists
if os.path.exists("/home/mayank/mydata.txt"):
    print("File exists")
# renaming file 
os.rename("/home/mayank/mydata.txt","/home/mayank/allgood.txt")

# Delete a file
os.remove("/home/mayank/ok.txt")

# Create a directory
os.mkdir("/home/mayank/alldata")

# to create nested directory
os.makedirs("/home/mayank/aaa/bbb/ccc")

# List files in a directory
files = os.listdir("/home/mayank/sab")
print(files)

# getting current working directory
print(os.getcwd())

# Change current working directory
os.chdir("/home/mayank/sab")

# getting current working directory
print(os.getcwd())

# Executing Shell Commands:
os.system("ls -l")

# getting absolute path of file
current_path = os.path.abspath("allgood.txt")
print(current_path)

# to remove non-empty directory we have to import shutil and use rmtree
import shutil
shutil.rmtree("/home/mayank/aaa")
