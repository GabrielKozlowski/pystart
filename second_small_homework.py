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