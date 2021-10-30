top_cities = ['New York City', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
# print(top_cities)
# print(top_cities[2])
# print(top_cities[-3])
# print(top_cities[2:4])


# book_ratings = [7, 9, 5, 6, 8]
# book_ratings.append(4)
# print(book_ratings)
#
# book_ratings = [7, 9, 5, 6, 8]
# book_ratings.insert(1, 10)
# print(book_ratings)
#
# book_ratings = [7, 9, 5, 6, 8]
# for numbers in book_ratings:
#     print('Numbers:', numbers)
#
# spendings = [32.45, 18.65, 23.45, 78.32, 5.23]
# sum = 0.0
# for spending in spendings:
#     sum += spending
# print('Money spend:', sum)

# spendings = [1346.0, 987.50, 1734.40, 2567.0, 3271.45, 2500.0, 2130.0, 2510.30, 2987.34, 3120.50, 4069.78, 1000.0]
#
# low = 0
# normal = 0
# high = 0
#
# for month in spendings:
#     if month < 1000.0:
#         low += 1
#     elif month <= 2500.0:
#         normal += 1
#     else:
#         high += 1
#
# print('Numbers of months with low spendings: ' + str(low) + ', normal spendings: ' + str(
#     normal) + ', high spendings: ' + str(high) + '.')
#
#
# first = input('Enter first number: ')
# second = input('Enter second number: ')
# print('Before swapping:', first, second)
# first, second = second, first
# print('After swapping:', first, second)

# random_numbers = [2, 5, 0, -3, 4]
# random_numbers.sort()
# print(random_numbers)
#
# for char in 'happy message':
#     print(char)
#
# invited_guests = ['Kate', 'Adam', 'Kerry', 'Joe', 'Anne', 'Marie']
# name = input('What is your name? ')
# if name in invited_guests:
#     print('Welcome!')
# else:
#     print('You are not invited!')
#
# invited_guests = ['Kate', 'Adam', 'Kerry', 'Joe', 'Anne', 'Marie']
# name = input('What is your name? ')
# if name not in invited_guests:
#     print('You are not invited!')
# else:
#     print('Welcome!')




# def func(mylist):
#     mylist[2] = 'green'
#
#
# lst = ['black', 'white', 'red', 'orange']
# func(lst)
# print(lst)
#
# first = second = third = "Boom!"
# print(second)
#
# my_list = [1, 2, 3]
# my_list.insert(1, 4)
# my_list.append(5)
# print(my_list)
#
# for num in range(1, 16, 2):
#     print(num, end = ",")

# print(36. * 10000000000000000000000)
#
# a = 'Exam'
# i = 0
# while i < len(a):
#     i += 1
# print(i)
#
# name = input()
# print(name == "Kate")

# x = 20
# if x != 10:
#     print("=")
#     if x < 6:
#         print("#")
#     elif x == 20:
#         print("#")
#     else:
#         print("#")
# else:
#     print("-" * 4)
#
#
# def swap(x, y):
#     x, y = y, x
#
#
# x = 5
# y = 10
# swap(x, y)
# print(x, y)
#
# print(7 % 4 ** 2 // 2)
#
# def fun(a, b, c):
#     return a * b * c
# print(fun(c=2, a=3, 6))

# tuple_first = (1, 2, 3)
# tuple_second = ('a', 'b')
# tuple_combined = tuple_first + tuple_second * 2
# print(tuple_combined)
#
# dict = {}
# dict[0] = 'Python'
# dict['numbers'] = [1, 2]
# print(dict)
#
# colors = ['red', 'blue', 'black']
# for color in colors:
#     if color != 'blue':
#         print(color, end=' ')
#
# dict1 = {'John': 27, 'Fruit': 'Banana'}
# dict2 = {'Fruit': 'Banana', 'John': 27}
# print(dict1 == dict2)
#
#
# def func(x):
#     for i in range(5):
#         yield i
#
#
# print(list(func(10)))

# age = input()
# print(age / 2)

# a = input()
# b = input()
# print(a + b * 2)

greeting = 'Honour!'
for ch in greeting:
  if ch == 'o':
    break
  print(ch)
else:
  print('Done!')

tupl = 1,2,'Three'
print(list(tupl))


a = 1
b = 3
print(a == b or a < b and not b != a)


full_name = 'king arthur'
print(full_name.title()[-6])


lst = [1, 2] * 3
print(len(lst))


val1 = 16
val2 = val1 << 2

print(val2)


def func(num):
    if num % 2 == 0:
        return True
    else:
        return False


print(not func(2))

x = 30


def change():
    global x
    x += 30
    print(30 + x)


print(x)
change()
print(x)
