# # >>>>>>>>>>>>>>> First task to do. <<<<<<<<<<<<<<<<
# # Convert degrees celsius to fahrenheit

# celsius = float(input('Please enter celsius degrees: '))
# fahrenheit = 2 * celsius + 32
# print(f'{celsius}°C = {fahrenheit}°F')

# #************************************************

# # >>>>>>>>>>>>>>> Second task to do. <<<<<<<<<<<<<<<<
# # Calculate the area of ​​a triangle by picking three vertices
#
# vertice_A_X = float(input('Please enter x value in vertice A: '))
# vertice_A_Y = float(input('Please enter y value in vertice A: '))
#
# vertice_B_X = float(input('Please enter x value in vertice B: '))
# vertice_B_Y = float(input('Please enter y value in vertice B: '))
#
# vertice_C_X = float(input('Please enter x value in vertice C: '))
# vertice_C_Y = float(input('Please enter y value in vertice C: '))
#
# area = 0.5 * ((vertice_B_X - vertice_A_X) * (vertice_C_Y - vertice_A_Y) - (vertice_B_Y - vertice_A_Y) * (vertice_C_X - vertice_A_X))
#
# print(f'Area of triangle: {area}')

# #****************************************************************************************

# # >>>>>>>>>>>>>>> Third task to do. <<<<<<<<<<<<<<<<
# # Print if number is divisible by 5, 11 or 5 and 11

# number = input('Please enter a number from 1 to 100: ')
#
# if number.isnumeric():
#     number = int(number)
#     if number % 5 == 0 and number % 11 == 0:
#         print(f'Number {number} is divide by 5 and 11')
#     elif number % 5 == 0:
#         print(f'Number {number} is divide by 5')
#     elif number % 11 == 0:
#         print(f'Number {number} is divide by 11')
#     # elif number % 5 != 0 and number % 11 != 0:
#     #     print(f'Number {number} is not divisible by 5 or 11')
#     else:
#         print(f'Number {number} is not divisible by 5 or 11')
# else:
#     print(f"[{number}] it's not a number")

# #****************************************************************************************

# # >>>>>>>>>>>>>>> Fourth task to do. <<<<<<<<<<<<<<<<
# # Print if number is positive or negative or zero
#
# number = input('Please enter a number from -100 to 100: ')
#
# if '-' in number:
#     number = number.lstrip('-')
#     if number.isnumeric():
#         number = '-' + number
#         number = int(number)
#         if number > 0:
#             print(f'Number {number} is positive')
#         elif number < 0:
#             print(f'Number {number} is negative')
#         else:
#             print(f'Number {number} is equal 0')
#     else:
#         print(f'{number} is not a number!')
# elif number.isnumeric():
#     number = int(number)
#     if number > 0:
#         print(f'Number {number} is positive')
#     elif number < 0:
#         print(f'Number {number} is negative')
#     else:
#         print(f'Number {number} is equal 0')
# else:
#     print(f'{number} is not a number!')

# #**********************************************************************************

# # >>>>>>>>>>>>>>> Fifth task to do. <<<<<<<<<<<<<<<<
# # Convert seconds to hours and format to 00:00

# time_in_seconds = 23400, 34200, 81000
#
# for time in time_in_seconds:
#     hours = time / 60 / 60
#     minutes = hours % 1 * 60
#     print(f'Its {int(hours)}:{int(minutes)}')
#
# def secondsToTime(seconds):
#     hours = seconds / 60 / 60
#     minutes = hours % 1 * 60
#     return f'Its {int(hours)}:{int(minutes)}'
#
#
# print(secondsToTime(34324))

# #**********************************************************************************

# # >>>>>>>>>>>>>>> Sixth task to do. <<<<<<<<<<<<<<<<
# # Do a math task.
#
# from math import pi, sqrt
#
# # # Enter value of point A and B
# value_Ax = int(input('Enter value of x in A point: '))
# value_Ay = int(input('Enter value of y in A point: '))
# value_Bx = int(input('Enter value of x in B point: '))
# value_By = int(input('Enter value of y in B point: '))
#
# # # Value of point C and D
# value_Cx = value_Ax
# value_Cy = value_By
# value_Dx = value_Bx
# value_Dy = value_Ay
# # # Length of segment AD and BD
# length_AD = sqrt((value_Dx - value_Ax) ** 2 + (value_Dy - value_Ay) ** 2)
# length_BD = sqrt((value_Dx - value_Bx) ** 2 + (value_Dy - value_By) ** 2)
#
# # # Calculation value x and y of center segment
# center_x = (value_Ax + value_Bx) / 2
# center_y = (value_Ay + value_By) / 2
# center_xy = center_x,center_y
# print(f'Center of segment: ({center_x}, {center_y})')
# # # Calculating radius value of segment
# radius = sqrt((center_x - value_Ax) ** 2 + (center_y - value_Ay) ** 2)
# print('Radius of segment: ',radius)
# # # Calculating field of a circle using the radius
# field = pi * radius ** 2
# print('Field: ',field)
# # # Calculating field of rectangle
# rectangle_field = length_AD * length_BD
# # # Calculating circuit of rectangle
# rectangle_circuit = length_AD * 2 + length_BD * 2
#
# print(f'Rectangle field = {rectangle_field}')
# print(f'Rectangle circuit = {rectangle_circuit}')

# #**********************************************************************************

# # >>>>>>>>>>>>>>> Seventh task to do. <<<<<<<<<<<<<<<<
# # Check inputed age, is it an adult and it the born year is a leap year.
#
# age_input = input("Please enter you'r age: ")
#
# if age_input.isnumeric():
#     age_input = int(age_input)
#     if age_input > 200:
#         print("You are definitely not that old !!")
#     else:
#         if age_input >= 18:
#             print("You are an adult")
#         else:
#             print("You are not an adult")
#
#         curent_year = 2022
#         born_year = curent_year - age_input
#         if born_year % 4 == 0 and born_year != 1900 and born_year != 2100:
#             print(f"Your born year {born_year} is a leap year")
#         else:
#             print(f"Your born year {born_year} is not a leap year")
# else:
#     print("Enter only the numbers!!!")

# #********************************************************************************

# # >>>>>>>>>>>>>>> Eighth task to do. <<<<<<<<<<<<<<<<
# # Check if input number is palindrome.

#
# numbers_input = input("Enter a number, we'll check if it's a palindromic number: ")
# list_numbers = list(numbers_input)
# reverse_list = list_numbers.copy()
# reverse_list.reverse()
#
# if numbers_input.isnumeric():
#
#     if len(list_numbers) % 2 == 0:
#
#         if list_numbers == reverse_list:
#             print(f"The number {numbers_input} it's palindromic")
#         else:
#             print(f"The number {numbers_input} it's not palindromic")
#
#     else:
#         print("The numbers must be even")
# else:
#     print("You must enter numbers !!")
#
# #******************************************************

