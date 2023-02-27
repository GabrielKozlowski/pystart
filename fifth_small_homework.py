#
# def word_counter(text):
#     words = text.split(' ')
#     return len(words)
#
# sentence = 'Ala ma kota i pozdrawiay wszystkie Ale i koty!!'
# print(word_counter(sentence))
# ##########################################################################
# volwes = 'a', 'ą', 'e', 'ę', 'i', 'o', 'u', 'ó', 'y'
# volwes = 'aąeęiouóy'
#
# def get_vowels(text):
#     volwes_from_text = set()
#     for word in text.lower():
#         if word in volwes:
#             volwes_from_text.add(word)
#     return volwes_from_text
#
# print(get_vowels('mamąibabcią'))



# ##########################################################################
# def check_if_primary(number):
#     if number > 1:
#         for n in range(2, number):
#             if number % n == 0:
#                 return False
#         return True
#     return False
#
# for n in range(1, 12):
#     print(n, check_if_primary(n))

#
# print(check_if_primary(1))
# print(check_if_primary(2))
# print(check_if_primary(3))
# print(check_if_primary(4))
# print(check_if_primary(5))
# ##########################################################################

