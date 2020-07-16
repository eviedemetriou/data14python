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

# Like a special if statement (if can do something do it otherwise do something else)
# try:
#     print("Trying to open this file...")
#     file = open("order.txt")
#     print("This file is open.")
# except FileNotFoundError as errmsg:  # Should be specific errors
#     print("Error!")
#     print(errmsg)
#     raise  # The error will be raised but we get whatever prints we expect to get too
# finally:
#     print("Finished handling everything.")  # Will print before error raised

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
#             print(line.lstrip("\n"))
#
#         opened_file.close()
#
#     except FileNotFoundError:
#         print("File cannot be found!")
#         raise

# open_and_print_file("order.txt")

#print(opened_file.readlines())

def open_and_print_file(filename):
    try:
        with open("order.txt") as opened_file:
            file_line_list = opened_file.readlines()

            for line in file_line_list:
                print(line.lstrip("\n"))

            #opened_file.close() # Not need in 'with' block

    except FileNotFoundError:
        print("File cannot be found!")
        raise


#with open("order.txt", "w") as opened_file:
#    opened_file.write("Cheeseburger\nPotato Salad")

#print(opened_file.readlines())

def append_to_file(filename, order):
    try:
        with open(filename, "w") as opened_file:
            opened_file.write(order + '\n')

    except TypeError:
        print("Order needs to be a string.")

print(append_to_file("order.txt", "Pasta"))
print(append_to_file("order.txt", "Kebab"))
