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
# # Create dictionary with temperature in Cities.
#
# cities = {}
# print('If You Enter "break" TO City Name, The Program Ends')
# while True:
#     name_of_city = input("\nEnter City Name: ")
#     if name_of_city == 'break':
#         break
#     temp_of_city = input("Enter Temperature In This City: ")
#     city = {name_of_city: temp_of_city}
#     cities.update(city)
#
# average_temp = []
#
# for name, temp in cities.items():
#     average_temp.append(int(temp))
#
# average_temp_value = sum(average_temp) / len(cities)
# sort_temp = sorted(average_temp)
# print(f'Average Temp: {average_temp_value:.1f}\nMax Temp: {sort_temp[-1]}\nMin Temp: {sort_temp[0]} ')

# # >>>>>>>>>>>>>>> Sixth task to do. <<<<<<<<<<<<<<<<
# # Create dictionary with Names

# names = []
# print('If You Enter "break" To Name, The Program Ends')
#
# while True:
#     name_to_add = input('Enter Name To Add: ').capitalize()
#     if name_to_add == 'Break':
#         break
#
#     names.append(name_to_add)
# dict_of_names = {}
# for name in names:
#     value = names.count(name)
#     person = {name: value}
#     dict_of_names.update(person)
#
# print(f"Dictionary Of Names: {dict_of_names}")
# dict_of_names = set(dict_of_names)
# dict_of_names = list(dict_of_names)
# print(f"List Of Unique Names  {sorted(dict_of_names)}")

# # >>>>>>>>>>>>>>> Seventh task to do. <<<<<<<<<<<<<<<
# # Check Even, Odd Numbers and add to list

# odd_numbers = []
# even_numbers = []
#
# while (number := int(input('Enter number, 0 ends program. : '))) != 0:
#     (even_numbers.append(number) if number % 2 == 0 else odd_numbers.append(number))
#
# print(f"List Of Odd Numbers: {odd_numbers}\nList Of Even Numbers: {even_numbers}")

# # >>>>>>>>>>>>>>> Eighth task to do. <<<<<<<<<<<<<<<<
# # Add product to basket from dictionary of products. Check amount and calculate value of bill
#
# products = {
#     'bread': 2.5,
#     'apples': 1.8,
#     'cheese': 4.2,
#     'juice': 3.8,
#     'butter': 6.2,
# }
#
# basket = {}
# while True:
#     for product, price in products.items():
#         print(f"{product.capitalize()} - {price}zł")
#     print('\nEnter "summarize" to end the program')
#     choice_product = input('What Product You Want Add To Your Basket?? : ').lower()
#     if choice_product == 'summarize':
#         break
#     choice_value = int(input('How Many ?? : '))
#
#     if choice_product not in products.keys():
#         print('This Product Does Not Exist')
#
#     stuff = {choice_product: {choice_value: (choice_value * products[choice_product])}}
#     basket.update(stuff)
#
# print('---' * 20)
# bill = 0
# for product, staff in basket.items():
#     for amount, price in staff.items():
#         print(f"You Bought {amount} x {product}")
#         bill += price
#
# print(f'To Pay: {bill:.2f}zł')

# # >>>>>>>>>>>>>>> Ninth task to do. <<<<<<<<<<<<<<<<
# # Encryption password
#
# encrypt = 3
#
# password = 'python is eazy'
# print(password)
# encrypted_password = []
# for word in password:
#     code_word = ord(word) + encrypt
#     encrypted_password.append(str(code_word))
#
# print(encrypted_password)
# real_password = ''
# for number in encrypted_password:
#     encode_word = chr(int(number) - encrypt)
#     real_password += (str(encode_word))
#
# print(real_password)

# # >>>>>>>>>>>>>>> Tenth task to do. <<<<<<<<<<<<<<<<
# # Remove all words starts with putted letter
#
# text = 'Python is the best program to learn. Python is eazy to use in automatic plays'
# print(text)
# text = text.lower().split()
#
# new_text = ''
# for word in text:
#     if not word.startswith('p'):
#         new_text += f"{word} "
#
# print(new_text)

# # >>>>>>>>>>>>>>> Eleventh task to do. <<<<<<<<<<<<<<<<
# # Check which word in two text are the same

# text1 = set('first name')
# text2 = set('last name')
# test = text1 & text2
# print(test)

# # >>>>>>>>>>>>>>> Twelfth task to do. <<<<<<<<<<<<<<<<
# # print word beloved word from text with coma.

# text = 'For ,learning ,python ,you ,need ,quiet ,and ,peace'
# print(text)
# text = text.replace(',', '\n')
# print(text)

# # >>>>>>>>>>>>>>> Thirteenth task to do. <<<<<<<<<<<<<<<<
# # check if string1 is equal to mixed string1
#
# word1 = 'basketball'
# word2 = 'lasbklbtae'
#
# word1 = sorted(word1)
# word2 = sorted(word2)
#
# if word1 == word2:
#     print('Equal !!')