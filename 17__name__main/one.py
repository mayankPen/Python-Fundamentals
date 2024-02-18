def func():
    print('func() in one.py')

print("Top level in one.py")
if __name__ == "__main__":
    print('One.py is being run directly.')
    print(__name__)
else:
    print('one.py is being imported into another module.')
    print(__name__)

