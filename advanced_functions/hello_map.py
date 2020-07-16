# # MAP FUNCTION
#
# def func(x):
#     return x^2 + 3
#
# print(func(2))
#
# # FILTER FUNCTION
#
# students = ["DAVID", "jOHN", "RICHARD"]
# result = filter(str.isupper, students)
# print(list(result))
#
# def func2(x):
#     return x % 2 == 0 and x % 3 == 0
# print(func2(6))
#
# numbers = list(range(1,100))
# result = filter(func2, numbers)
# print(list(result))
#
# # LAMBDA FUNCTIONS
#
# #add = lambda num1, num2 : num1 + num2
# #print(add)
#
# result = map(lambda x: x * x + 3, numbers)
# print(list(result))

savings = [12.0, 123.00, 352.00, 35.00]
bonus = map(lambda x: round(x * 1.1, 2), savings)
print(list(bonus))

even_savings = filter(lambda x: x % 2 == 0, savings)
print(list(even_savings))