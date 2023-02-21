# # >>>>>>>>>>>>>>> First task to do. <<<<<<<<<<<<<<<<
# # Create list of friends and print that list sorted alphabetically
# ## Create list of friends names

# friends_names = ['Mirek', 'Łukasz', 'Rafał', 'Paweł', 'Grzesiek']

#  ## Create variable with sorted friends list
# sorted_list = sorted(friends_names)

# ## Print sorted list
# print(sorted_list)
# #***************************************************************************

# # >>>>>>>>>>>>>>> Second task to do. <<<<<<<<<<<<<<<<
# # Create dictionary with keys as fruits and value as price. Print value of apples and banana

# products = {
#     'Apples': 3.50,
#     'Orange': 4.70,
#     'Kivi': 1.20,
#     'Banana': 1.75,
#     'Watermelon': 6.0
# }
#
# print(f"Apples price: {products['Apples']}")
# print(f"Banana price: {products['Banana']}")
#
# #*****************************************************************************


# # >>>>>>>>>>>>>>> Third task to do. <<<<<<<<<<<<<<<<
# # Create dictionary with info of your favorite movies (title, production year, director).
# # Next delete Steven Spielberg movie.
#
# favorite_movies = {
#     'Steven Spielberg':
#         [
#             {
#                 'title': 'Saving Private Ryan',
#                 'production_year': 1998,
#             },
#             {
#                 'title': 'Minority Report',
#                 'production_year': 2002,
#             }
#         ],
#     'Christopher Nolan':
#         [
#             {
#                 'title': 'Interstellar',
#                 'production_year': 2014,
#             },
#             {
#                 'title': 'Inception',
#                 'production_year': 2010,
#             }
#         ]
# }
#
# print(favorite_movies)
# del favorite_movies['Steven Spielberg'][:]
# print(favorite_movies)

# #***************************************************************************

# # >>>>>>>>>>>>>>> Fourth task to do. <<<<<<<<<<<<<<<<
# # Create dictionary with info of your favorite animals (animal name, number of legs).
# # Find animal that has the most legs and print animal name and value of legs.
#
# favorite_animals = {
#     'dog': 4,
#     'horse': 4,
#     'spider': 8,
#     'millipede': 100,
#     'cat': 4,
# }
# value = 0
# animal_with_the_most_legs = ''
#
# for animal, legs in favorite_animals.items():
#     if legs > value:
#         value = legs
#         animal_with_the_most_legs = animal
#
# print(animal_with_the_most_legs)
# #*********************************************************************************

# # >>>>>>>>>>>>>>> Fifth task to do. <<<<<<<<<<<<<<<<
# # Create dictionary with info of your favorite animals (animal name, race).
# # Find animal that has the longest name and print animal name and rase.
#
# home_animals = {
#     'Tigra': 'dog',
#     'Hultek': 'cat',
#     'Chester': 'rabbit',
#     'Diana': 'dog',
#
# }
# animal_name = ''
#
# for name in home_animals.keys():
#     if len(name) > len(animal_name):
#         animal_name = name
#
# print(animal_name, home_animals[animal_name])

# #**************************************************************

# # >>>>>>>>>>>>>>> Sixth task to do. <<<<<<<<<<<<<<<<
# # Create dictionary with info of your favorite countries (country name, capitol, language).
# # Add a new country to dict and print new dictionary.

#
#
# info = '''
#
# Welcome to dictionary of information about your favorite countries.
# Press number to function.
#
# 1 - Show dictionary info
# 2 - Add new country to dictionary
# 3 - Delete country from dictionary
# 4 - Quit program
#
# '''
# dictionary = []
#
# while True:
#
#     try:
#         choices_number = int(input(info))
#     except ValueError:
#         print('Wrong number')
#     else:
#         if choices_number == 1:
#             if len(dictionary) == 0:
#                 print('Nothing in here')
#             else:
#                 for country in dictionary:
#                     print(country)
#
#         elif choices_number == 2:
#             country_name = input('Enter name of country: ')
#             capitol_name = input('Enter name of capitol: ')
#             language_name = input('Enter name of language: ')
#             print()
#             new_country_info = {
#                 'country': country_name,
#                 'capitol': capitol_name,
#                 'language': language_name,
#             }
#
#             if new_country_info not in dictionary:
#                 dictionary.append(new_country_info)
#             else:
#                 print('The country is already in dictionary ')
#
#         elif choices_number == 3:
#             country_to_delete = input('Enter country name to delete: ')
#             for number, country in enumerate(dictionary):
#                 if country_to_delete in country['country']:
#                     del dictionary[number]
#                 else:
#                     pass
#
#         elif choices_number == 4:
#             break

# #*****************************************************************************************

# # >>>>>>>>>>>>>>> Seventh task to do. <<<<<<<<<<<<<<<<
# # "Word jumble"
# from random import choice, shuffle
#
#
# words = ['money', 'python', 'bike', 'friends', 'variable', 'coding', 'yerba', 'poland', 'keyboard']
#
#
# random_word = choice(words)
# list_word = list(random_word)
# shuffle(list_word)
#
#
# play = input('Want to play "Word Jumble" y/n ?? ').lower()
# counter = 0
# if play == 'y':
#     print(list_word)
#
#     while counter < 3:
#         answer = input('Enter answer: ')
#         counter += 1
#         if answer == random_word:
#             print(f"Congrats. You guessed !! You needed {counter} trial/s ")
#             break
#         else:
#             print('Try again')
#             continue
#
# else:
#     quit()
#
# #******************************************************************************************

# # >>>>>>>>>>>>>>> Eighth task to do. <<<<<<<<<<<<<<<<
# # Write simply diners generator
# from random import choice
#
# dishes = {
#     'soup': ['tomato', 'cucumber', 'chicken'],
#     'lunch': ['meet balls', 'doves', 'schnitzel'],
#     'dessert': ['icecream', 'cake', 'pudding'],
# }
#
# soup_choice = choice(dishes['soup'])
# lunch_choice = choice(dishes['lunch'])
# dessert_choice = choice(dishes['dessert'])
#
# print(f"Soup: {soup_choice}\nLunch: {lunch_choice}\nDessert: {dessert_choice}")

# #****************************************************************************************

# # >>>>>>>>>>>>>>> Ninth task to do. <<<<<<<<<<<<<<<<
# # Chose a random card from 52 card deck
#
# from random import choice
# cards = []
# nuber_of_cards = ["2", "3", "4", "5", "6", "7", "8", "9", "J", "Q", "K", "A"]
# type_of_cards = [chr(9824), chr(9827), chr(9829), chr(9830)]
#
# for type_of_card in type_of_cards:
#     for number_of_card in nuber_of_cards:
#         cards.append(f"{type_of_card}{number_of_card}")
#
# print(cards)
#
# random_card = f"{choice(nuber_of_cards)} {choice(type_of_card)}"
# print("Random Choice: ", random_card)

# #******************************************************************************************

# # >>>>>>>>>>>>>>> Tenth and Eleventh task to do. <<<<<<<<<<<<<<<<
# # Draws a random country name and asking for its capitol, If answer is correct print Good Answer
# from random import choice
#
# countries_name = ['Poland', 'Ghana', 'Togo']
#
#
# choice = choice(countries_name)
#
# print(f"Draws Country: {choice}")
# trials = 0
# points = 3
# while points >= 0:
#     user_answer = input(f'Enter a capitol name for {choice}: ').lower()
#     trials += 1
#     if choice == 'Poland':
#         if user_answer == 'warsaw':
#             print(f"Good Answer! Trials: {trials}")
#             break
#         else:
#             print("Bad Answer... Try Again.")
#             points -= 1
#             continue
#     elif choice == 'Ghana':
#         if user_answer == 'akra':
#             print(f"Good Answer! Trials: {trials}")
#             break
#         else:
#             print("Bad Answer... Try Again.")
#             points -= 1
#             continue
#     elif choice == 'Togo':
#         if user_answer == 'lome':
#             print(f"Good Answer! Trials: {trials}")
#             break
#         else:
#             print("Bad Answer... Try Again.")
#             points -= 1
#             continue
#     else:
#         print('Error')
#         break
#
# if points == 3:
#     print('You are awesome ')
# elif points == 2:
#     print('Just one mistake')
# elif points == 1:
#     print('One point not bad')
# else:
#     print('You be better next time')
# #**********************************************************************







