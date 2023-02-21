#
# items = set()
#
# for _ in range(5):
#     item = input('Add new item to you bag: ')
#     items.add(item)
#     print(items)
#
#
# # ================================================================================
# email_list = []
#
# for _ in range(4):
#     email = input("Add new email: ")
#     if '@' in email and (email.endswith('.pl') or email.endswith('.com')):
#         email_list.append(email)
#     else:
#         print('Wrong email adress !!')
#
# print('Email List: ',email_list)
# email_set = set(email_list)
# print('Email Set: ', email_set)

# # ================================================================================
#
# divide_by_3 = set(range(3, 101, 3))
# divide_by_5 = set(range(5, 101, 5))
#
# print(divide_by_3 & divide_by_5)

# #====================================================================
# mama = set('mama')
# tata = set('tata')
#
# c = mama & tata
# b = mama ^ tata
# print(b)
# print(c)

# #====================================================================

# students = {
#     ("Piotr", "Kowalczyk"),
#     ("Katarzyna", "Mazur"),
#     ("Tomasz", "Adamski"),
#     ("Agnieszka", "Kaczmarek"),
#     ("Krzysztof", "Krawczyk"),
#
# }
#
# going_on_trip = {
#     ("Katarzyna", "Mazur"),
#     ("Tomasz", "Adamski"),
#     ("Krzysztof", "Krawczyk"),
# }
#
# stay_in_school = students - going_on_trip
# print(stay_in_school)

# #====================================================================





