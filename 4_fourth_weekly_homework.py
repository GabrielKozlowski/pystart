# # >>>>>>>>>>>>>>> First task to do. <<<<<<<<<<<<<<<<
# # Create Math Operations Program

# info = '''
#     Welcome To Program
#     You Can Do Math Operations
#     Enter Your Values And Choice
#     Operations To Do
#
#     1 - Add
#     2 - Subtract
#     3 - Multiply
#     4 - Divide
#     5 - Exit
# '''
# print(info)
#
# while True:
#     value1 = int(input('\nEnter first value: '))
#     operation = int(input('Choice a operation to do '))
#     value2 = int(input('Enter second value: '))
#
#     if operation == 1:
#         value = value1 + value2
#         print(f"Result of {value1} + {value2} = {value}")
#     elif operation == 2:
#         value = value1 - value2
#         print(f"Result of {value1} - {value2} = {value}")
#     elif operation == 3:
#         value = value1 * value2
#         print(f"Result of {value1} * {value2} = {value}")
#     elif operation == 4:
#         value = ("Can't divide by 0" if value2 == 0 else value1 / value2)
#         print(f"Result of {value1} / {value2} = {value}")
#     elif operation == 5:
#         exit()
#     else:
#         print('Bad Operation Number...')


# # >>>>>>>>>>>>>>> Second task to do. <<<<<<<<<<<<<<<<
# # Change Value To Kilograms, Ounces, Pounds


# info = '''
#      Welcome To Program
#      You Can Check Value Of
#      Kilograms, Ounces, Pounds
#      Operations To Do And
#      Enter Your Values To Convert
#
#
#      1 - Kilograms To Ounces
#      2 - Ounces To Kilograms
#      3 - Kilograms to Pounds
#      4 - Pounds To Kilograms
#      5 - Ounces To Pounds
#      6 - Pounds To Ounces
# '''
#
# print(info)
#
# while True:
#     value = int(input('\nEnter Value To Convert: '))
#     choice = int(input('Enter Number Of Operations To Do: '))
#     if choice == 1:
#         result = value * 35.274
#         print(f'Convert {value} Kilograms To Ounces = {result}')
#
#     elif choice == 2:
#         result = value / 35.274
#         print(f'Convert {value} Ounces To Kilograms = {result:.3f}')
#
#     elif choice == 3:
#         result = value * 2.20462
#         print(f'Convert {value} Kilograms To Pounds = {result}')
#
#     elif choice == 4:
#         result = value / 2.20462
#         print(f'Convert {value} Pounds To Kilograms = {result:.3f}')
#
#     elif choice == 5:
#         result = value * 0.0625
#         print(f'Convert {value} Ounces To Pounds = {result}')
#
#     elif choice == 6:
#         result = value / 0.0625
#         print(f'Convert {value} Pounds To Ounces = {result:.3f}')
#     else:
#         print('Bad Operation Number !')


# # >>>>>>>>>>>>>>> Third task to do. <<<<<<<<<<<<<<<<
# # Check If Enter Password Is Correct

# password = 'python-is-the-best'
#
# while (user_answer := input('Enter password: ')) != password:
#     print('Password is not corrected !!')
# print('Password Corrected')

# # >>>>>>>>>>>>>>> Fourth task to do. <<<<<<<<<<<<<<<<
# # Program For ATM Options
#
# info = '''
#      Welcome To ATM
#      Enter Number Of Operation
#
#      1 - Check Your Account Amount
#      2 - Add Cash To Account
#      3 - Withdraw Cash From Account
#      4 - Quit
#
# '''
# print(info)
#
# value_of_account = 0
#
# pin_access = '2355'
# check_pin = input('Enter Pin...: ')
#
# if check_pin == pin_access:
#     while (choice_operation := int(input('What Operation You Choice ?: '))) != 4:
#         if choice_operation == 1:
#             print(f"Your Account Amount: {value_of_account}")
#         elif choice_operation == 2:
#             value = int(input('Enter Value To Add: '))
#             value_of_account += value
#         elif choice_operation == 3:
#             value = (int(input('Enter Value To Withdraw: ')) if value_of_account > 0 else "You Don't Have Enough Money")
#             value_of_account -= value
#         elif choice_operation == 4:
#             quit()
#         else:
#             print("Bad Operation Number")
# else:
#     print('Bad Pin...')


# # >>>>>>>>>>>>>>> Fifth task to do. <<<<<<<<<<<<<<<<

# # >>>>>>>>>>>>>>> Sixth task to do. <<<<<<<<<<<<<<<<

# # >>>>>>>>>>>>>>> Seventh task to do. <<<<<<<<<<<<<<<

# # >>>>>>>>>>>>>>> Eighth task to do. <<<<<<<<<<<<<<<<

# # >>>>>>>>>>>>>>> Ninth task to do. <<<<<<<<<<<<<<<<



