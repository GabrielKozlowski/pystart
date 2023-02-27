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


# # >>>>>>>>>>>>>>> Second task to do. <<<<<<<<<<<<<<<<
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


# # >>>>>>>>>>>>>>> Third task to do. <<<<<<<<<<<<<<<<
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


# # >>>>>>>>>>>>>>> Fourth task to do. <<<<<<<<<<<<<<<<
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
#     # For Loop For Word In Spli Text
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

# # >>>>>>>>>>>>>>> Fifth task to do. <<<<<<<<<<<<<<<<


# # >>>>>>>>>>>>>>> Sixth task to do. <<<<<<<<<<<<<<<<


# # >>>>>>>>>>>>>>> Seventh task to do. <<<<<<<<<<<<<<<


# # >>>>>>>>>>>>>>> Eighth task to do. <<<<<<<<<<<<<<<<


# # >>>>>>>>>>>>>>> Ninth task to do. <<<<<<<<<<<<<<<<


# # >>>>>>>>>>>>>>> Tenth task to do. <<<<<<<<<<<<<<<<



