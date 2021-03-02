# #Def method:
# def add(num1, num2):
#     return num1 + num2
#
# print(add(2, 3))
#
# #Lambda method:
# addition = lambda num1, num2: num1 + num2
# print(addition(2, 3))

#Map
#Structure - map(function, iterable)
def square_func(num):
    return num ** 2

numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

#def func
#squared_numbers = map(square_func, numbers_list)

#Lambda
squared_numbers = map(lambda x: x ** 2, numbers_list)

print(list(squared_numbers))

salary = [230, 350, 540, 430]
bonus = map(lambda x: round(x * 1.1), salary)
print(list(bonus))