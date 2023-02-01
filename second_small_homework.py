#
# animal = 'owca'
# print(animal)
# print(type(animal))
#
# animal2 = 'owca',
# print(animal2)
# print(type(animal2))
#
# fruits = 'apple','orange','banana','water melon', 'cherry',
#
# print(fruits[0],fruits[2],fruits[4])

# #**********************************************************************

# names = 'Alicja', "Ewa", "Aleksandra"
# inputed_name = input("Podaj imię: ").capitalize()
#
# if inputed_name in names:
#     print('To imie znajduje się na liście!')
# else:
#     print("To imie nie znajduje się na liście!")
# #**********************************************************************

# fruits = 'mango', 'banana', 'cherry', 'orange', 'apple', 'peach', 'lemon', 'grapefruit'
# print(fruits[0])
# print(fruits[0:2])
# print(fruits[0:4:2])
# print(fruits[:4:2])
# print(fruits[::2])
# print(fruits[::-1])
# print(fruits[::-2])
# #**********************************************************************
# one_hundred_numbers = tuple(range(1, 101))
# print(one_hundred_numbers, '\n')
# print(one_hundred_numbers[:10], '\n')
# print(one_hundred_numbers[-10:], '\n')
# print(one_hundred_numbers[-1:-11:-1], '\n')
# print(one_hundred_numbers[::2], '\n')
# print(one_hundred_numbers[::-2], '\n')
# #**********************************************************************
# assessments = (4, 5, 6, 6, 4, 5, 5, 6, 6, 3, 4)
#
# print(sorted(assessments))
#
# average = (sum(assessments) / len(assessments))
# print(f'{average:.2f}')
# if average >= 4.75:
#     print('Congratulations You get a certificate with a red stripe')
# else:
#     print("You do not receive a certificate with a red stripe")
# #**********************************************************************
# names = "Alex", "Ewa", "Alicja", "Gabriel"
# for index, name in enumerate(names):
#     print(index,name)
#
# print('*'* 50)
#
# numbers = (56, 7, 4, 2, 43, 6, 7, 8, 98, 344, 24, 545, 63, 57)
#
# for number in numbers:
#     if number % 4 == 0 or number % 5 == 0:
#         print(number)
# print('-'* 50)
# for name in names:
#     if len(name) > 5:
#         print(name)
# print('*'* 50)
#
# for counter in reversed(range(1, 5)):
#     for digit in range(1, counter + 1):
#         print(digit, end=' ')
#     print()
#
# #**********************************************************************

# name = input("Enter you'r name: ").lower()
#
# if (name.endswith('a') or name.startswith('nel')) and not name.startswith('kuba'):
#     print(f"Witam panią. {name.capitalize()}")
# else:
#     print(f"Witam pana. {name.capitalize()}")
#
# password = input("Enter you'r password: ").replace('a', '@').replace('s', '$').replace('o', '0')
# print(password)
#
# text = 'Pies to najlepszy przyjaciel człowieka, lecz nie każdy pies o tym wie'
# print(text.lower().count('pies'))
#
# shopping = "12 kilogramów jabłek, 10 kilogramów gruszek, 20 kilogramów śliwek".split(' ')
# weight = 0
# for a in shopping:
#     if a.isnumeric():
#         a = int(a)
#         weight += a
#
# print(weight)
# # Create a christmas tree :)
# xx = '''
#     1
#    121
#   12321
#  1234321
# 123454321
# '''
# levels = 10
#
# if levels <= 10:
#     for line in range(1, levels):
#         if line == 1:
#             numbers = '{}'.format(line)
#             print(' ' * (levels - line), numbers)
#         else:
#             reversed_numbers = numbers[::-1]
#             numbers += '{}'.format(line)
#             print(' ' * (levels - line), numbers + reversed_numbers)
# else:
#     print("To many levels !!!")
# # ***************************************************************

# number = int(input("Entry a number to check: "))
# isPrime = True
# if number > 1:
#     for n in range(2, number):
#         if number % n == 0:
#             isPrime = False
#             break
#
# if isPrime:
#     print(f"Number {number} is a prime number")
# else:
#     print(f"Number {number} is not a prime number")

# #***************************************************


# bands = ['system of a down', 'linking park', 'Coldplay']
# print(bands)
#
# bands[0] = '50cent'
# print(bands)
#
# del bands[0]
#
# bands.append('50cent')
# bands.append('System of a down')
# print('Coldplay' in bands)
# print('Sanah' in bands)
#
# bands.remove('System of a down')
# print(bands)
#
# text = list('dowolnynapis')
# print(text)
# text = ''.join(text)
# print(text)

#******************************************************
#
# names = ["asia", "baSIa", "WoJtEk", "krYSIA"]
# proper_names = []
#
# for name in names:
#     proper_names.append(name.title())
#
# print(names)
# print(proper_names)
#
# cities = ['Warsaw', 'Cracow', 'Gdansk']
# new_cities = ['Berlin', 'London']
#
# all_cities_plus = cities + new_cities
# cities.extend(new_cities)
#
# countries = ['Polska', 'Niemcy', 'Francja']
# capitals = ['Warszawa', 'Berlin', 'Paryż']
#
# print("Państwo - Stolica")
#
# for country, capital in zip(countries, capitals):
#     print(country, '-', capital)

#********************************************************************
#
# sentence = input('Enter your sentence: ')
#
# sentence_words = len(sentence.split(' '))
# sentence_len = len(sentence),
# print('Len of words', sentence_words)
# print('ELen of letters', sentence_len)
#
#
# ####
# numbers_list = []
# number_of_numbers = 5
#
# for r in range(number_of_numbers):
#     user_number = int(input(f'Enter {r+1} number: '))
#     numbers_list.append(user_number)
#
# print(numbers_list)
# print(f"Najmniejsza liczba to {min(numbers_list)}")
# print(f"Największa liczba to {max(numbers_list)}")
# print(f"Średnia liczb to {(sum(numbers_list) / len(numbers_list))}")

# people_list = []
# person_name_list = []
#
# for _ in range(3):
#     user_answer = input('Enter Name and surname: ')
#     people_list.append(user_answer)

# ## first way
# for person in people_list:
#     person_data = person.split(' ')
#     if person_data[0] not in person_name_list:
#         person_name_list.append(person_data[0])

# ## another way

# for person in people_list:
#     first_name, last_name = person.split(' ')
#     if first_name not in person_name_list:
#         person_name_list.append(first_name)
#
#
# sorted_person_name_list = sorted(person_name_list, reverse=True)
# print(sorted_person_name_list)
# print(person_name_list)

#**********************************************
