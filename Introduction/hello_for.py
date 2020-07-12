Chinese_menu = {
    10: {"dish": "egg fried rice", "price": 6.16},
    11: {"dish": "noodles", "price": 7.50},
    12: {"dish": "salad", "price": 5}
}

for key in Chinese_menu:
    print(Chinese_menu[key]["dish"], ":  ", Chinese_menu[key]["price"])
print("\n")

for key in Chinese_menu:
    for subkey in Chinese_menu[key]:
        print(Chinese_menu[key][subkey])

print("\n")
print(list(range(10)))
# OR
for num in range(10):
    print(num)
