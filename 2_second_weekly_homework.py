# # >>>>>>>>>>>>>>> First and second task to do. <<<<<<<<<<<<<<<<
# # Print even numbers from input
# # Print sum, amount, ratio and average of number from input

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



