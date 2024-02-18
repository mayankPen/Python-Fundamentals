# Understanding Exceptions:
# 1.Exceptions are errors that occur during program execution, disrupting the normal flow.
# 2.Python raises specific exceptions (like ZeroDivisionError or FileNotFoundError) to signal 
#   these errors.
# 3.Handling exceptions gracefully prevents your program from crashing and allows you to provide 
#   meaningful feedback to the user.

# Basic try...except Syntax:

# try:
#     # Code that might raise an exception
# except ExceptionType1:
#     # Handle ExceptionType1
# except ExceptionType2:
#     # Handle ExceptionType2
# ...
# else:
#     # Code that executes if no exception occurs
# finally:
#     # Code that always executes, regardless of exceptions


# 1.try block: Encloses code that might raise exceptions.
# 2.except block(s): Indicate the type of exception(s) you want to handle (e.g., ZeroDivisionError, 
#   ValueError).
# 3.Exception handling inside except: Perform recovery actions or provide informative messages.
# 4.else block (optional): Executes code if no exception occurs in the try block.
# 5.finally block (optional): Code that always executes, regardless of exceptions, often used 
#   for cleanup (e.g., closing files).

# Handling file errors:

try:
    with open("myfile.txt", "r") as f:
        content = f.read()
except FileNotFoundError:
    print("Error: File not found.")
except IOError:
    print("Error: An I/O error occurred.")
finally:
    if f is not None:
        f.close()  # Ensure file is closed, even if exceptions occur


# Ignoring Exceptions:
try:
    # Code that may raise an exception
except Exception:
    pass  # Ignoring the exception


# Specific Exception Handling:
try:
    # Code that may raise a specific exception
except ValueError:
    # Code to handle the ValueError exception


# Nested Exception Handling:
try:
    # Code that may raise an exception
    try:
        # Code that may raise another exception
    except AnotherException:
        # Code to handle the inner exception
except Exception:
    # Code to handle the outer exception


# Raising Custom Exceptions:
    
try:
    # Code that may raise an exception
    if some_condition:
        raise CustomException("Custom error message")
except CustomException as e:
    # Handling the custom exception
    print("Custom exception occurred:", e)


# Handling Exceptions and Accessing the Error Message:
try:
    # Code that may raise an exception
except Exception as e:
    # Accessing the error message using the 'e' variable
    print("An error occurred:", e)


# Multiple Exceptions Handling:
try:
    # Code that may raise multiple exceptions
except (ValueError, TypeError):
    # Code to handle either ValueError or TypeError


