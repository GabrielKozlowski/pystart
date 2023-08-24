#
# items = set()
#
# for _ in range(5):
#     item = input('Add new item to you bag: ')
#     items.add(item)
#     print(items)
#
#
# # ================================================================================
# email_list = []
#
# for _ in range(4):
#     email = input("Add new email: ")
#     if '@' in email and (email.endswith('.pl') or email.endswith('.com')):
#         email_list.append(email)
#     else:
#         print('Wrong email adress !!')
#
# print('Email List: ',email_list)
# email_set = set(email_list)
# print('Email Set: ', email_set)
import random
# # ================================================================================
#
# divide_by_3 = set(range(3, 101, 3))
# divide_by_5 = set(range(5, 101, 5))
#
# print(divide_by_3 & divide_by_5)

# #====================================================================
# mama = set('mama')
# tata = set('tata')
#
# c = mama & tata
# b = mama ^ tata
# print(b)
# print(c)

# #====================================================================

# students = {
#     ("Piotr", "Kowalczyk"),
#     ("Katarzyna", "Mazur"),
#     ("Tomasz", "Adamski"),
#     ("Agnieszka", "Kaczmarek"),
#     ("Krzysztof", "Krawczyk"),
#
# }
#
# going_on_trip = {
#     ("Katarzyna", "Mazur"),
#     ("Tomasz", "Adamski"),
#     ("Krzysztof", "Krawczyk"),
# }
#
# stay_in_school = students - going_on_trip
# print(stay_in_school)

# #====================================================================
# numbers_list = []
# counter = 0
#
# while counter < 10:
#     number = int(input('Enter next number: '))
#     if number >= 0:
#         counter += 1
#         numbers_list.append(number)
#
# print(f"List Of Numbers: ", numbers_list)
# print(f"Min number is: {min(numbers_list)}")
# print(f"Max number is: {max(numbers_list)}")
# #====================================================================

# list_of_numbers = []
# last_number = None
#
#
# while True:
#     number = int(input('Enter number bigger than last one: '))
#     if last_number is not None and number < last_number:
#         break
#
#     last_number = number
#     list_of_numbers.append(number)
#
# print(sum(list_of_numbers) / len(list_of_numbers))
# #====================================================================
# from random import randint
#
# trials = 0
# random_number = random.randint(1, 101)
#
# while True:
#     trials += 1
#     user_guess = int(input('\nTry Guess A Number 1 - 100: '))
#     if user_guess == random_number:
#         print(f"Congratulations, You Guess The Number !!. You Needs {trials} Trials.")
#         break
#     elif user_guess > random_number:
#         print("Your Answer Is Too Big. Try Again")
#     elif user_guess < random_number:
#         print("Your Answer Is To Small. Try Again")
#     else:
#         print("Bad Answer. Try Again...")
# #====================================================================

# if (n := int(input('Podaj liczbe: '))) % 2 == 0:
#     print(f"Liczba {n} jest parzysta")

# #===================================================================
# value = []
# while (n := int(input('Podaj lizbę: '))) != 0:
#     value.append(n)
#
# print(sum(value))
# #===================================================================
# total = False
# value = 'Man' if total else 'Woman'
# print(value)
#
# sala = True
# age = 20 if sala else 19
# print(age)
# sala = False
# print(20 if sala else 19)
# #===================================================================

# base = 2000
#
# years_of_word = int(input('Enter Your Years Of Work: '))
# amount_of_sales_products = int(input('How Many Products You Sale In This Month: '))
# hours_in_month = int(input('Enter How Many Hours You Work In This Month: '))
#
# seniority_bonus = 0.1 if years_of_word > 2 else 0.02
# sales_bonus = 0.25 if amount_of_sales_products > 30 else 0
# hours_bonus = 0.08 if hours_in_month > 160 and years_of_word > 1 else 0.02
#
# salary = base + base * seniority_bonus + base * sales_bonus + base * hours_bonus
# print(f"Your Salary In This Month: {salary}")
# #########################################################

#  ##   #With WALRUS operator !!
# base = 2000
#
# seniority_bonus = 0.1 if (years_of_word := int(input('Enter Your Years Of Work: '))) > 2 else 0.02
# sales_bonus = 0.25 if (amount_of_sales_products := int(input('How Many Products You Sale In This Month: '))) > 30 else 0
# hours_bonus = 0.08 if (hours_in_month := int(input('Enter How Many Hours You Work In This Month: '))) > 160 and years_of_word  > 1 else 0.02
#
# salary = base + base * seniority_bonus + base * sales_bonus + base * hours_bonus
# print(f"Your Salary In This Month: {salary}")

# #===================================================================
#
# list1 = [1,2,3,4,5,6]
# list2 = [7,8,4,3,5,0]
#
# print(list(zip(list1, list2)))
# print(tuple(zip(list1, list2)))
# print(set(zip(list1, list2)))
# print(dict(zip(list1, list2)))
#
# for l1, l2 in zip(list1, list2):
#     print(l1, l2)

# #===================================================================

# pessel = '51062488907'
# control = '13791379131'
#
# pessel.replace('', ' ')
# mnożnik.replace('', ' ')
# numbers_sum = 0
# if len(pessel) == 11:
#     for number, power in zip(pessel, control):
#         value = int(number) * int(power)
#         numbers_sum += value
# print(numbers_sum)
# if str(numbers_sum).endswith('0'):
#     print(f"This pessel {pessel}: is correct")
# else:
#     print('Pessel is not correct !!')
# #===================================================================
