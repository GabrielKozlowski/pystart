# # >>>>>>>>>>>>>>> First and second task to do. <<<<<<<<<<<<<<<<
# # Print even numbers from input
# # Print sum, amount, ratio and average of number from input
#
# numbers = int(input("Enter integer number:  "))
# sum_of_number = 0
# amount_of_number = 0
# ratio_of_number = 1
#
# for number in range(1, numbers + 1):
#     if number % 2 == 0:
#         sum_of_number += number
#         amount_of_number += 1
#         ratio_of_number = number * ratio_of_number
#         print(f"{number},")
#
# average_of_number = sum_of_number / amount_of_number
# print('\n')
# print(f'Sum of numbers: {sum_of_number}')
# print(f'Amount of numbers: {amount_of_number}')
# print(f'Average of numbers: {average_of_number}')
# print(f'Ratio of numbers: {ratio_of_number}')

# #************************************************

# # >>>>>>>>>>>>>>> Third task to do. <<<<<<<<<<<<<<<<
# # Print number power to 2,3,4 and 5,  from input

# number = int(input("Enter number to power: "))
#
# for x in range(1, 6):
#     result = number ** x
#     print(f"Number ({number}) power by {x} - {result}")

# #************************************************
# # >>>>>>>>>>>>>>> Fourth task to do. <<<<<<<<<<<<<<<<
# # Print all letters from input text and show ASCII number

# text = input("Enter text: ")
#
# for letter in text:
#     ord_letter = ord(letter)
#     print(f"Letter: '{letter}' = ASCII number: {ord_letter}")

# #************************************************
# # >>>>>>>>>>>>>>> Fifth task to do. <<<<<<<<<<<<<<<<
# # Check is it prime number

# number = int(input("Enter a integer number: "))
# flag = False
# if number > 1:
#     for i in range(2, number):
#         if (number % i) == 0:
#             flag = True
#             break
#
# if flag:
#     print(f"Number: {number} is not a prime")
# else:
#     print(f"Number: {number} is prime number !!")
# #************************************************
# # >>>>>>>>>>>>>>> Fifth task to do. <<<<<<<<<<<<<<<<
# # Create tuple and add numbers multiplied by 6, print some numbers.
#
# numbers = ()
# for number in range(12, 1024, 6):
#     numb = (number,)
#     numbers += numb
#
# sum_of_numbers = len(numbers)
# print(numbers)
# print(f"Sum of numbers: {sum_of_numbers}")
# print('First three numbers: ', numbers[:3])
# print("Penultimate number: ", numbers[-2])
# print(f"Every sixth number in the range from the third to the last number: {numbers[3:1024:6]}")
# print(f"Every third number from the end: {numbers[::-3]}")
# print("Sum of last ten numbers:", (sum(numbers[-10:]) / len(numbers[-10:])))
# #************************************************
# # >>>>>>>>>>>>>>> Sixth task to do. <<<<<<<<<<<<<<<<
# #  Use position in tuple and print them
#
# person = ('Gabriel', 'Kozlowski', '33')
#
# print(f"Imię: {person[0]}\nNazwisko: {person[1]}\nWiek: {person[2]}")

# #************************************************
# # >>>>>>>>>>>>>>> Seventh task to do. <<<<<<<<<<<<<<<<
# #  Add numbers in tuple and print result
#
# first_number_tuple = (1, 2, 3)
# second_number_tuple = (4, 5, 6)
# third_number_tuple = (7, 8, 9)
#
# print(f"{first_number_tuple[0]} + {first_number_tuple[1]} + {first_number_tuple[2]} = {sum(first_number_tuple)}")
# print(f"{second_number_tuple[0]} + {second_number_tuple[1]} + {second_number_tuple[2]} = {sum(second_number_tuple)}")
# print(f"{third_number_tuple[0]} + {third_number_tuple[1]} + {third_number_tuple[2]} = {sum(third_number_tuple)}")
# print('\n')
#
# calculations = (1, 2, 3), (4, 5, 6), (7, 8, 9)
#
# for calculation in calculations:
#     print(f"{calculation[0]} + {calculation[1]} + {calculation[2]} = {sum(calculation)}")

# #************************************************
# # >>>>>>>>>>>>>>> Eighth task to do. <<<<<<<<<<<<<<<<
# #  Do some operations on strings
# # 1
# text = input("Enter the text spaces and punctuation marks: ")
#
# print(text[::-1])
# print('\n')
#
# # 2
# punctuation_marks = ('!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '-', '+', '=', ',', '.', '?', '/', '|', ';', ' ', ':', '>', '<')
# fixed_text = ''
# for t in text:
#     if t in punctuation_marks:
#         t = t.replace(t, '')
#         fixed_text += t
#     else:
#         fixed_text += t
#
# print(fixed_text)
#
# # 3 & 4
#
# message = input("Enter some text: ")
#
# split_message = message.split(' ')
# print(f'Split message: {split_message}\n')
#
# snake_message = ''
# list_words = []
# without_vowels = ''
# vowels = 'aeiouóyąę'
#
#
# for x in range(0, len(split_message)):
#
#
#     if x % 2 == 1:
#         modified_x = split_message[x].upper()
#         snake_message += (modified_x + ' ')
#
#         if modified_x[0] == modified_x[-1] and len(modified_x) > 2:
#             list_words.append(modified_x.lower())
#
#     else:
#         modified_x = split_message[x].lower()
#         snake_message += (modified_x + ' ')
#
#         if modified_x[0] == modified_x[-1] and len(modified_x) > 2:
#             list_words.append(modified_x.lower())
#
#     for word in split_message[x].lower():
#
#         if word in vowels:
#             word = ' '
#             without_vowels += word
#         else:
#             without_vowels += word
#
# print(f"Snake message : {snake_message}")
# print(f'List of words with the same first and last letter: {list_words}')
# print(f"Without vowels: {without_vowels} ")
#

# #************************************************

