character = {'first_name': 'Grzegorz', 'last_name': 'Brzęczyszczykiewicz', 'run': '9'}
tests = {'run': '10', 'shoot': '9', 'hide': '3'}
print(character)
character.update(tests)
print(character)

print(character.get('run'))

capitals = {'Poland': 'Warsaw', 'Maroko': 'Rabat', 'Estonia': 'Tallin'}

for country in capitals:
    print(country)
    print(capitals[country])

for country, capital in capitals.items():
    print(country)
    print(capital)
