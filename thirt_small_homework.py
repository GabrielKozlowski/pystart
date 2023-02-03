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
s = 'ula'
s = 'ala'

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

workers = [
    {
        'id': 1,
        'job_title': 'junior developer',
        'name': 'John',
        'programming_language': ['python']
    },
    {
        'id': 2,
        'job_title': 'senior developer',
        'name': 'Mark',
        'programming_language': ['python', 'php']
    },
    {
        'id': 3,
        'job_title': 'stuff developer',
        'name': 'Alex',
        'programming_language': ['php', 'javascript', 'python']
    },
    {
        'id': 4,
        'job_title': 'junior developer',
        'name': 'Bart',
        'programming_language': ['javascript', 'php']
    },
    {
        'id': 5,
        'job_title': 'senior developer',
        'name': 'Carl',
        'programming_language': ['python', 'javascript']
    },
    {
        'id': 6,
        'job_title': 'junior developer',
        'name': 'Martha',
        'programming_language': ['php', 'javascript']
    }
]
language_dict = {}

for worker in workers:

    for code_language in worker['programming_language']:

        if code_language not in language_dict:
            language_dict[code_language] = {
                'quantity': 0,
                'names': []
            }

        language_dict[code_language]['quantity'] += 1
        language_dict[code_language]['names'].append(worker['name'])

print(language_dict)


