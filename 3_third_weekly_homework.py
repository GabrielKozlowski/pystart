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
# print(animal_name)

# #**************************************************************

# # >>>>>>>>>>>>>>> Sixth task to do. <<<<<<<<<<<<<<<<
# # Create dictionary with info of your favorite countries (country name, capitol, language).
# # Add a new country to dict and print new dictionary.

#
#
# info = '''
#
# Welcome to dictionary of your favorite countries info.
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
