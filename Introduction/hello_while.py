counter = 0
while counter < 10:
    print(counter)
    if counter == 6:
        break
    counter += 1

age = "six"
while not age.isnumeric():
    age = input("Your age please: ")
    if not age.isnumeric():
        print("Enter a numeric age!")

