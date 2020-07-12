hw = "Hello world!"

name = input("Insert your name:  \n")
age = int(input("Insert your age:  \n"))
sibl = int(input("Insert the number of siblings you have:  \n"))
decNum = float(input("Insert your favourite decimal number:  \n"))
animal = input("Insert your favourite animal:  \n")

print(f"{name}, {age}, {sibl}, {decNum}, {animal} \n")


hw = "    Hello world!!!     "
print(hw.count(" "))
print(hw.lower())
print(hw.upper())
print(hw.capitalize())
print(hw.replace("o", "oooooo"))
print(hw.strip())  # or .lstrip() or .rstrip()
print(hw.strip().upper())