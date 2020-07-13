# LISTS

shopping_list = ["bananas", "apples", "oranges", "watermelon", 8, True]

shopping_list[4] = "mango"
shopping_list.append("lemon")
del shopping_list[:3]
print(shopping_list.index(True))
print(shopping_list)
print(type(shopping_list), "\n")

# TUPLES

colour = ("blue", "red", "green", "orange")

print(colour.count("purple"))
print(colour.index("orange"))
print(colour, "\n")

# DICTIONARIES

my_dic = {1: "gorilla", 2: "elephant", 3: "dolphin", 4: "horse", 5: "eagle", "animal": "chicken"}
del my_dic["animal"]
my_dic.pop(4)
my_dic[6] = "zebra"
my_dic[4] = "dolphin"
print(my_dic)
print(my_dic.keys())
print(my_dic.values(), "\n")

data14dic = {
    "weeks": 10,
    "location": "remote",
    "trainees_age": {"Evie": 28, "Charlotte": 22, "Katie": 22, "Jade": 22},
    "subjects": ["SQL", "Data Concepts", "Agile", "Python", "Git"]
}
print(data14dic)
print(data14dic["trainees_age"])
print(data14dic["trainees_age"]["Evie"])
print(data14dic["subjects"][2], "\n")

# SETS

cars = {"renault", "bmw", "audi", "mercedes", "ferrari"}

cars.pop()  # random item removed
cars.add("jaguar")
cars.remove("bmw")  # might not work if removed above
print(cars)
