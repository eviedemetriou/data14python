# ZeroDivision error
# Indentation error
# Name not found
# ModuleNotFound error
# Syntax error
# Type error
# Index error
# Key error
# Attribute error
# RecursionError
# FileNotFound error

## TRY - EXCEPT: like a special if statement
## TRY will run until it finds error and then EXCEPT runs
# try:
#     print("Trying to open this file...")
#     file = open("order.txt")
#     print("This file is open.")
# except FileNotFoundError as errmsg:  # errmsg provides the error msg so we don't lose it
#     print("Error!")
#     print(errmsg)
#     raise  # The error will be raised, code will stop, however this block runs as normal
# finally:  # will run before error is raised
#     print("Finished handling everything.")

# t - Read mode (default)
# w - write mode (if no file, creates one; if file, truncates)
# x - create mode (if file, fails)
# a - append mode (if no file, create one; if file, append)
# t - text mode
# b - binary mode
# + - reading and writing

# def open_and_print_file(filename):
#     try:
#         opened_file = open(filename, "r")
#         file_line_list = opened_file.readlines()
#
#         for line in file_line_list:
#             print(line.rstrip("\n"))  # avoides extra line spaces
#
#         opened_file.close()  # have to close file
#
#     except FileNotFoundError:
#         print("File cannot be found!")
#         raise

# file = open("order.txt")
# print(file.readlines())  # returns a list of all lines
# print(file.readline())  # reads one line at a time, which is lost from the buffer
# print(file.readline())  # will print the second line, which will be lost (if don't assign it)

def open_and_print_file(filename):
    try:
        with open(filename, "r") as opened_file:
            # print(opened_file.readlines())  # reads whole file as a list
            file_line_list = opened_file.readlines()  # assign it so can iterate through lines

            for line in file_line_list:
                print(line.rstrip("\n"))  # avoids extra line spaces

            #opened_file.close() # Not need in 'with' block
    except FileNotFoundError:
        print("File cannot be found!")
        raise


# With 'w' and 'a' modes don't need FileNotFoundError because a new file will be created
def write_to_file(filename):
    try:
        with open(filename, "w") as opened_file:
            opened_file.write("Cheeseburger\nPotato Salad")
    except TypeError:
        print("Order needs to be a string")

def append_to_file(filename, order):
    try:
        with open(filename, "a") as opened_file:
            opened_file.write(order + '\n')
    except TypeError:
        print("Order needs to be a string.")

print(append_to_file("order.txt", "Pasta"))
print(append_to_file("order.txt", "Kebab"))

