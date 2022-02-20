# print('hello, there!')

# user_age = int(input('What is your age? '))
# if user_age > 30:
#    print('You are over 30 years old')
#    print('Sorry, you do not qualify')
# elif user_age == 30:
#    print('You are exactly 30 years old')
#    print('You will need to meet additional conditions to qualify')
# else:
#    print('You are 30 years old or younger')
#    print('Congratulations, you qualify')

# user_age = int(input('What is your age? '))
# user_country = input('What is your country? ')
#
# if user_age < 25 and user_country == 'Germany':
#     print('You can apply for a German student exchange programme')
# else:
#     print('Sorry, you do not qualify')

# answer_a = input('Do you like travelling? y/n: ')
# if answer_a == 'y':
#     answer_b = input('And do you like South Africa? y/n: ')
#     if answer_b == 'y':
#         print('Excellent! you can win a ticket to South Africa!')
#     else:
#         print('Sorry to hear that!')
# else:
#     print('Sorry to hear that')


# purchase_date = int(input('How many days ago have you purchased the item? '))
# used_item = input('Have you used the item at all [y/n]? ')
# broken_down = input('Has the item broken down on its own [y/n]? ')
#
# if purchase_date <= 10 and not used_item:
#     print('You can get a refund')
# elif purchase_date > 0 and broken_down:
#     print('You can get a refund ')
# else:
#     print('You cannot get a refund')

# purchase_days_ago = int(input('How many days ago have you purchased the item? '))
# is_used = input('Have you used the item at all [y/n]? ')
# is_broken = input('Has the item broken down on its own [y/n]? ')
#
# if (is_broken == 'y' or (purchase_days_ago <= 10 and is_used == 'n')):
#     print('You can get a refund.')
# else:
#     print('You cannot get a refund.')


# counter = 1
# while counter < 11:
#     print(counter)
#     counter += 1
# print('Finished!')
#
# secret_number = 14
# user_input = int(input('Try to guess the secret number from 0 to 20: '))
# while user_input != secret_number:
#     print('Wrong')
#     user_input = int(input('Try to guess the secret number from 0 to 20: '))
# print('Perfect! You have guessed the secret number.')

# for letter in 'hello':
#     print('Current letter', letter)
#
#
# for counter in range(1, 11):
#     print(counter)
# print('Finished')
#
# while True:
#     name = input('Enter your name or EXIT to close the program: ')
#     if (name == 'EXIT'):
#         break
#     print('Hello', name)

# for i in range(1, 21):
#     if i % 5 == 0:
#         continue
#     print(i)

# for i in range(11):
#     pass
#
#
#
# answer = 0
# while True:
#     answer = int(input('When was Python 1.0 released? '))
#     if answer > 1994:
#         print('It was earlier than that!')
#     elif answer < 1994:
#         print('It was later than that!')
#     else:
#         print('Correct!')
#         break

# i = 0
# while i <= 10:
#     i += 1
#     if i % 2 == 0:
#         break
#     print('*')

# x = 1
# x = x == x
# print(x)

# a = 5
# b = 1
# c = a > b or b < a and a == 1
# print(c)

# choice = int(input('Pick a number: '))
# if number == 3:
#     print('Good choice')
# else:
#     print('You could have chosen better')
# else:
#     print('No luck this time')

# answer_a = int(input('Try to guess the first number: '))
#
# if answer_a == 8:
#     answer_b = int(input('Correct! Now, guess the second number: '))
#     if answer_b == 5:
#         print('You won!')
#     else:
#         print('You only got one number right. So close!')
# else:
#     print('Wrong!')

# counter = 1
# while counter < 11:
#   print(counter)

# for x in 'i am having fun today':
#   print(x)

# for i in range(1, 12):
#     if i % 4 == 0:
#         continue
#     print(i, end='-')

# i = 1
# while i < 5:
#     print(i, end=' ')
#     i += 1
# else:
#     print(i, end=' ')

for a in range(1, 6):
    for b in range(1, 10):
         if (a == b):
           print(a)