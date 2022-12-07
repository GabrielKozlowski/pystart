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