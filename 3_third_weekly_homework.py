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



