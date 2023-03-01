# # >>>>>>>>>>>>>>> First task to do. <<<<<<<<<<<<<<<<
# # Create Function. Get two list and return sum of lists index
#
#
# def sum_lists(list1: list, list2: list) -> list:
#     """
#     This Function Get Two List And Sum Index Value
#     :param list1: List of Integers
#     :param list2: List of Integers
#     :return: Sum in list index
#     """
#     # Create new list to return value
#     new_list = []
#     # Connect two lists to one, with zip function
#     connected_lists = zip(list1, list2)
#     # For loop for tuple value in list
#     for value in connected_lists:
#         result = sum(value)
#         new_list.append(result)
#
#     return new_list
#
#
# # Create Lists For Function
# list_a = [2, 4, 6, 8, 11]
# list_b = [6, 4, 7, 9, 19]
#
# print(sum_lists(list_a, list_b))
#


# # >>>>>>>>>>>>>>> Second task to do. <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# # Create Function. Get list of numbers and return list with only even numbers
#
# def get_even_numbers(number_list: list) -> list:
#     """
#     This Function Returns Only Even Numbers From List
#     :param number_list: List Of Numbers
#     :return: List Of Even Numbers
#     """
#     # Create new list to return
#     new_number_list = []
#     # For loop in number list
#     for number in number_list:
#         # Check if number is even
#         if number % 2 == 0:
#             # Add even number to new list
#             new_number_list.append(number)
#     return new_number_list
#
#
# # Create List Of Numbers To Function
# list1 = list(range(9, 39))
# print(get_even_numbers(list1))


# # >>>>>>>>>>>>>>> Third task to do. <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# # Create Function. Get string and return only strings with length 4-8
#
# def check_string(text: str) -> str:
#     """
#     This Function Checks Length Of String And Returns Only 4-8 Length
#     :param text: String To Check
#     :return: String With Length 4 to 8
#     """
#     # Change Text To Lower Case And Split Words With ' '
#     split_text = text.lower().split(' ')
#     # Create New List For Words
#     new_text = []
#     # For Loop For Word In Text
#     for word in split_text:
#         # Check If Word Length Is Bigger Than 4 And Smaller Than 8
#         if 4 <= len(word) <= 8:
#             # Append Word To New List
#             new_text.append(word)
#     # Change List To String And Return It
#     return ' '.join(new_text)
#
#
# # Create Text To Function
# text1 = 'Alicja want two dogs, alsatian and labrador'
# print(check_string(text1))


# # >>>>>>>>>>>>>>> Fourth task to do. <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# # Create Function. Check string and count letters in brackets
#
# def count_letter(text: str, start: str = '(', end: str = ')') -> int:
#     """
#     This Function Count Numbers Of Letters In Brackets
#     :param text: Text With Brackets
#     :param start: First Bracket In Text
#     :param end: last Bracket In Text
#     :return: Numbers Of Letters In All Brackets
#     """
#     # Create New Variable To Count Letters
#     number_of_letters = 0
#     # Split Words In Text
#     split_text = text.split(' ')
#     # For Loop For Word In Split Text
#     for word in split_text:
#         # Check If Word Starts And Ends With Bracket
#         if word.startswith(start) and word.endswith(end):
#             # Add numbers Of Letters In Word And Minus 2 For Brackets
#             number_of_letters += (len(word) - 2)
#
#     return number_of_letters
#
#
# # Create Text For Function
# text1 = '(ala) ma (kota)'
# print(count_letter(text1))
# text2 = '<> kod <103>'
# print(count_letter(text2, '<', '>'))
# text3 = 'abrakadabra'
# print(count_letter(text3))
#

# # >>>>>>>>>>>>>>> Fifth task to do. <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# # Create Function. Get From User Value In Percent And Print Mark
#
# def count_mark(percent: int) -> str:
#     """
#     This Function Checks How Many Percent It Is And Return String
#     :param percent: Int Of Percent
#     :return: Information Of THe Mark
#     """
#     # Check Percent Value And Return Message
#     if percent < 45:
#         return "Your mark is: 1"
#     elif 45 <= percent < 55:
#         return "Your mark is: 2"
#     elif 55 <= percent < 80:
#         return "Your mark is: 3"
#     elif 80 <= percent < 90:
#         return "Your mark is: 4"
#     elif 90 <= percent < 95:
#         return "Your mark is: 5"
#     else:
#         return "Your mark is: 6"
#
#
# # Create Value For Function
# percent_of_exam = 65
# print(count_mark(percent_of_exam))

# # >>>>>>>>>>>>>>> Sixth task to do. <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# # Create Function. Get Two Tuples With Value Of X And Y And Return Calculated Value
# from math import sqrt
#
#
# def count_section(point1: tuple = (0, 0), point2: tuple = (0, 0)) -> float:
#     """
#     This Function Get Two Tuples And Calculate The Length Of The Section
#     :param point1: Tuple With Two Value x1 , y1
#     :param point2: Tuple With Two Value x2 , y2
#     :return: Result Of Calculated Value, Float
#     """
#     # Create A Variable And Doing Math Calculate
#     section = sqrt((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2)
#     return section
#
#
# # Create Tuples With Value
# first_point = (-7, -2)
# second_point = (4, 4)
# print(count_section(first_point, second_point))

# # >>>>>>>>>>>>>>> Seventh task to do. <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# # Create Function. Calculate Kilometer To Miles
#
# def kilometers_to_miles(value: int = 1) -> float:
#     """
#     This Function Calculate Kilometers Value To Miles Value
#     :param value: Value Of Kilometers To Calculate
#     :return: Miles In Float
#     """
#     # Create Variable And Calculate Value
#     miles = value * 0.621371192
#     return miles
#
# #
# def miles_to_kilometers(value: int = 1) -> float:
#     """
#     This Function Calculate Miles Value To Kilometers Value
#     :param value: Value Of Miles To Calculate
#     :return: Kilometers In Float
#     """
#     # Create Variable And Calculate Value
#     kilometers = value / 0.621371192
#     return kilometers


# value_to_calculate = 10
# km_to_ml = kilometers_to_miles(value_to_calculate)
# ml_to_km = miles_to_kilometers(value_to_calculate)
# print(f"Kilometers: {value_to_calculate} = {km_to_ml:.2f} Miles")
# print(f"Miles: {value_to_calculate} = {ml_to_km:.2f} Kilometers")

# # >>>>>>>>>>>>>>> Eighth task to do. <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# # Create Function. Get List With Value And Return Dict With Total,Mean,Max,Min Value
#
#
# def get_value_from_list(list1: list) -> dict:
#     """
#     This Function Get List And Return Dict With Total, Mean, Max, Min Value
#     :param list1: List With Value To Count
#     :return: Dict With Value Total, Mean, Max, Min
#     """
#
#     total = len(list1)
#     mean = sum(list1) / total
#     dict_to_return = {
#         "total": total,
#         "mean": mean,
#         "max value": max(list1),
#         "min value": min(list1)
#     }
#
#     return dict_to_return
#
#
# list_for_function = [2, 3, 6, 8, 9, 43, 23, 65, 777, 22]
# print(get_value_from_list(list_for_function))

# # >>>>>>>>>>>>>>> Ninth task to do. <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# # Create Function. Get String And Revers It
#
#
# def revers_string(text: str) -> str:
#     """
#     This Function Get String And Revers It
#     :param text: String To Revers
#     :return: Reversed String
#     """
#     # Create List For Letters
#     reversed_string_list = []
#     # Loop For Adding Last Letter To New List
#     for i in range(1, len(text) + 1):
#         reversed_string_list.append(text[-i])
#     # Join Letters And Return String
#     return ''.join(reversed_string_list)
#
#
# # Create String For Function
# text_to_func = 'coding in Python'
# print(revers_string(text_to_func))
# # # ============================================================================
# # Create Function. Get String And Revers Letters In Words
#
#
# def revers_string(text: str, separator=' ') -> str:
#     """
#     This Function Get String And Revers Letters In Words
#     :param text: String To Revers
#     :param separator: What Separator Is In String
#     :return: Reversed String
#     """
#     # Split Words Using Separator From User
#     split_text = text.split(sep=separator)
#     # Create List For Text
#     reversed_string_list = []
#     # Loop For Word In Text
#     for word in split_text:
#         # Create List For Reversed Word
#         word_list = []
#         # Loop For Adding Last Letter To New Word List
#         for i in range(1, len(word) + 1):
#             word_list.append(word[-i])
#         # Adding New Word To List For Text, With Join Func
#         reversed_string_list.append(''.join(word_list))
#     # Join Words And Return String
#     return ' '.join(reversed_string_list)
#
#
# # Create String For Function
# text_to_func = 'coding in Python'
# text_to_func2 = 'coding-in-Python'
#
# print(revers_string(text_to_func))
# # Adding Separator
# print(revers_string(text_to_func2, separator='-'))


# # >>>>>>>>>>>>>>> Tenth task to do. <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# Create Function. Get Numer Sort It And Return From The Smallest To The Largest
#
# def sorted_number(numb: int = 1) -> int:
#     """
#     This Function Revers Number And Return It From The Smallest To The Largest
#     :param numb: Number To Revers, More Than 9
#     :return: Reversed Number From The Smallest To The Largest
#     """
#     # Create List For Numbers
#     list_of_number = []
#     # Convert Int To Str And loop It
#     for number in str(numb):
#         # Append Str Number To List
#         list_of_number.append(number)
#     # Sorted List
#     list_of_number = sorted(list_of_number)
#     # Join String, Convert To Integer And Return.
#     return int(''.join(list_of_number))
#
#
# # Create variable With Number To Func
# number_to_func = 372418695
# print('Number to sort:', number_to_func)
# print('Sorted number:', sorted_number(number_to_func))

# # >>>>>>>>>>>>>>> Eleventh task to do. <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# # Create Function. Get Numbers List, Check If Number Is Positive Or Negative, Change Value And Return

#
# def changing_numbers_value(list1: list) -> list:
#     """
#     This Function Convert Numbers Value In List To The Opposite
#     :param list1: list With Numbers
#     :return: Numbers List With Opposite Value
#     """
#     # Create New List For Converted Numbers
#     changed_list = []
#     # Loop for Each Number In List
#     for number in list1:
#         # Check If Number Is Positive Or Negative And Change It, And Append To New List
#         changed_list.append(abs(number)) if number < 0 else changed_list.append(-abs(number))
#
#     return changed_list
#
#
# # Create List With Numbers For Function
# numbers_list_to_func = [2, -5, 6, -8, 9, -34, 61]
# print(changing_numbers_value(numbers_list_to_func))

# # >>>>>>>>>>>>>>> Twelfth task to do. <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# # Create Function. Get List With String Value And Convert It To Integer.
# # Create Function. Get List With Integer Value And Convert It To String.
#
# def change_list_elements_to_string(list1: list) -> list:
#     """
#     This Function Get List And Change Value To String
#     :param list1: List With Integer Value For Convert To String
#     :return: List With String Value
#     """
#     # Create New List For String Item
#     new_list = []
#     # Loop For Getting Number From List
#     for item in list1:
#         # Append String Item To New List
#         new_list.append(str(item))
#
#     return new_list
#
#
# def change_list_elements_to_integer(list1: list) -> list:
#     """
#     This Function Get List And Change Value To Integer
#     :param list1: List With String Value For Convert To Integer
#     :return: List With Integer Value
#     """
#     # Create New List For Integer Item
#     new_list = []
#     # Loop For String Item From List
#     for item in list1:
#         # Append Converted String Item To Integer
#         new_list.append(int(item))
#
#     return new_list
#
#
# # Create List With Numbers
# number_list_for_func = [1, 2, 3, 4, 5, 6, 7]
# print(change_list_elements_to_string(number_list_for_func))
# # Create List With String Items
# string_list_for_func = ['1', '2', '3', '4', '5', '6', '7', '8']
# print(change_list_elements_to_integer(string_list_for_func))

# # >>>>>>>>>>>>>>> Thirteen task to do. <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# # Create Function. Get Number To Sum It. Add All Earlier Numbers To Number. Sum It And Return
#
#
# def sum_to(number: int) -> int:
#     """
#     This Function Adding First Number To Next One. Ends When Added Last Number.
#     :param number: It's Last Number For Adding.
#     :return: Sum Of All Added Numbers.
#     """
#     # Check If Number Is Equal To 0. This Is For Ending Recursion
#     if number == 0:
#         return 0
#     # Return And Doing Recursion
#     return number + sum_to(number - 1)
#
#
# # Create Variable With Number To Function
# number_to_sum = 9
# print(sum_to(number_to_sum))

# # >>>>>>>>>>>>>>> Fourth task to do. <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# # Create Function. Get Pin And Check It If Len Of Pin It's Four
#
# def check_pin(pin: int) -> bool:
#     """
#     This Function Check If Pin Has Four Numbers
#     :param pin: Four Numbers To Check
#     :return: True Or False
#     """
#     # Check If String Len Of Pin Is Not Equal To Four
#     if len(str(pin)) != 4:
#         return False
#
#     return True
#
#
# # Create Variable OF Number To Func
# pin_to_check = 8272
# print(check_pin(pin_to_check))
###################################################################################

