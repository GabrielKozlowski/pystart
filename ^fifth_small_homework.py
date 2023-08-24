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
# from math import ceil
#
#
# def get_divisors(number, start=2):
#     divisors = set()
#     for divisor in range(start, ceil(number / 2) + 1):
#         if number % divisor == 0:
#             divisors.add(divisor)
#     return divisors
#
#
# def get_common_divisors(number1, number2, start=2):
#     divisor1 = get_divisors(number1, start)
#     divisor2 = get_divisors(number2, start)
#
#     return divisor1 & divisor2
#
#
# number1 = int(input('Number1: '))
# number2 = int(input('Number2: '))
# minimum = int(input('Start: '))
#
# print(number1, get_divisors(number1))
# print(number2, get_divisors(number2))
#
# print(get_common_divisors(number1, number2, minimum))

# ##########################################################################
# def calculate_common_divisor(number1, number2):
#     if number2 == 0:
#         return number1
#
#     else:
#         return calculate_common_divisor(number2, (number1 % number2))
#
#
# print(calculate_common_divisor(3, 6))
# print(calculate_common_divisor(3, 6))

# ##########################################################################

# def multiply(a, b=2):
#     return (a * b)
#
#
# print(multiply(2))
# print(multiply(2, 3))

# ##########################################################################
#
# def repeater_text(text, delimiter=',', repeat=1):
#     new_text = ''
#     for _ in range(0, repeat):
#         new_text += text
#         new_text += delimiter
#     new_text = new_text[:-1]
#     return new_text
#
#
# word = 'Alicja'
#
# print(repeater_text(word))
# print(repeater_text(word, repeat=3))
# print(repeater_text(word, delimiter='-', repeat=5))
# ##########################################################################

#
# def power(number: int) -> int:
#     """
#     This function multiply number if is bigger than 0
#     :param number: number to power
#     :return: results of multiply
#     """
#     if number == 0:
#         return 1
#
#     return number * power(number - 1)
#
#
# print(power(5))
# ##########################################################################
#
#
# def count_price_for_kwh(time: float, price: float = 1.03) -> float:
#     """
#     This function calculate price for kwh of electric:
#     :param time: How many hours used
#     :param price: Value of one hour in kilowatts
#     :return: float of calculate result
#     """
#     return time * price
#
#
# print(count_price_for_kwh(20))
# ##########################################################################

#
# def count_numbers(numbers: list, count_odd: bool = True, count_even: bool = True) -> int:
#     """
#     This function check how many numbers is with those arguments.
#     :param numbers: List of numbers .
#     :param count_odd: This argument count only odd numbers in list.
#     :param count_even: This argument count only even numbers in list.
#     :return: List of numbers with accept argument.
#     """
#     numbers_counter = 0
#
#     for n in numbers:
#         if n % 2 == 0 and count_even:
#             numbers_counter += 1
#         elif n % 2 != 0 and count_odd:
#             numbers_counter += 1
#
#     return numbers_counter
#
# numbers_list = list(range(1, 31))
#
# print(count_numbers(numbers_list))
# print(count_numbers(numbers_list, count_odd=False))
# print(count_numbers(numbers_list, count_even=False))

# ##########################################################################


