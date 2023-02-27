# character = {'first_name': 'Grzegorz', 'last_name': 'Brzęczyszczykiewicz', 'run': '9'}
# tests = {'run': '10', 'shoot': '9', 'hide': '3'}
# print(character)
# character.update(tests)
# print(character)
#
# print(character.get('run'))
#
# capitals = {'Poland': 'Warsaw', 'Maroko': 'Rabat', 'Estonia': 'Tallin'}
#
# for country in capitals:
#     print(country)
#     print(capitals[country])
#
# for country, capital in capitals.items():
#     print(country)
#     print(capital)
# #**********************************************************
import random
#
# s = 'ula'
# s = 'ala'

# message = '''
# Welcome
# You can translate some words to
# English or Polish
# '''
#
# words = {
#     "dog": "pies",
#     "cat": "kot",
#     "car": "auto",
#     "red": "czerwony",
#     "blue": "niebieski",
# }
# print(message)
# language = input("What language do you want to translate into, PL or ENG? ")
# word = input("Enter word to translate: ")
#
# translated_word = None
#
# for english_word, polish_word in words.items():
#     if language.lower() == 'eng' and english_word == word:
#         translated_word = polish_word
#
#     elif language.lower() == 'pl' and polish_word == word:
#         translated_word = english_word
#
# if translated_word is not None:
#     print(f"The translated word is [{translated_word}]")
# else:
#     print("I don't know this word")
# #******************************************************************


# sentence = input('Enter a sentence ')
# sentence = 'raz ja raz ty a raz ja i ona'
# sentence_dict = {word: sentence.split(' ').count(word) for word in sentence.split(' ')}
#
# print(sentence_dict)
# #------------------------------------
# sentence = 'Python to wpaniały język Python to język szybki i wydajny'
# words = sentence.split(' ')
# word_counter = {}
# for word in words:
#     word_counter[word] = word_counter.get(word, 0) + 1
#
# print(word_counter)
# #------------------------------------
# sentence = 'Python to wpaniały język Python to język szybki i wydajny'
#
# sentence_dict = {word: sentence.split(' ').count(word) for word in sentence.split(' ')}
# print(sentence_dict)
# # **********************************************************************************************
# workers = [
#     {
#         'id': 1,
#         'job_title': 'junior developer',
#         'name': 'John',
#         'programming_language': ['python']
#     },
#     {
#         'id': 2,
#         'job_title': 'senior developer',
#         'name': 'Mark',
#         'programming_language': ['python', 'php']
#     },
#     {
#         'id': 3,
#         'job_title': 'stuff developer',
#         'name': 'Alex',
#         'programming_language': ['php', 'javascript', 'python']
#     },
#     {
#         'id': 4,
#         'job_title': 'junior developer',
#         'name': 'Bart',
#         'programming_language': ['javascript', 'php']
#     },
#     {
#         'id': 5,
#         'job_title': 'senior developer',
#         'name': 'Carl',
#         'programming_language': ['python', 'javascript']
#     },
#     {
#         'id': 6,
#         'job_title': 'junior developer',
#         'name': 'Martha',
#         'programming_language': ['php', 'javascript']
#     }
# ]
# language_dict = {}
#
# for worker in workers:
#
#     for code_language in worker['programming_language']:
#
#         if code_language not in language_dict:
#             language_dict[code_language] = {
#                 'quantity': 0,
#                 'names': []
#             }
#
#         language_dict[code_language]['quantity'] += 1
#         language_dict[code_language]['names'].append(worker['name'])
#
# print(language_dict)
# #********************************************************************************************
# from random import choice
#
# print("Play with computer in Paper-Rock-Scissors \n")
# value = 'paper', 'scissors', 'rock'
#
# player_choice = input("Enter Your chose [paper-scissors-rock]: ").lower()
# computer_choice = choice(value)
#
# print(f"Player chose: {player_choice} --- Computer chose: {computer_choice}\n")
#
# if player_choice not in value:
#     print('Wrong value !')
#     quit()
#
# if player_choice == computer_choice:
#     print("It's a Draw!!")
#
# elif (player_choice == 'paper' and computer_choice == 'rock') or \
#         (player_choice == 'rock' and computer_choice == 'scissors') or \
#         (player_choice == 'scissors' and computer_choice == 'paper'):
#     print('Player wins')
#
# else:
#     print('Computer wins')
# # *************************************************************************
#
# from random import randint
# from math import ceil, floor, sqrt, pow
#
# print('Draw random number from 1-100:')
#
# random_number = random.randint(1, 100)
# square_number = pow(random_number, 2)
# sqrt_number = sqrt(random_number)
# result_sqrt_number = 0
#
#
# print(f"Random number: {random_number} ")
# print(f"Sqrt of {random_number} is: {square_number}")
# print(f"Element of {random_number} : {sqrt_number}")
# print(f"Element of {random_number} to ceil: {ceil(sqrt_number)}")
# print(f"Element of {random_number} to floor: {floor(sqrt_number)}")