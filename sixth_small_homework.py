#
# def sum_it(*args: int, limit: int = 0) -> int:
#     """
#     This Function Sum Numbers Bigger Than Limit And Return Result.
#     :param args: Numbers To Add.
#     :param limit: Minimal Number Value For Adding.
#     :return: Sum Of Added Numbers.
#     """
#     total = 0
#     for arg in args:
#         if arg > limit:
#             total += arg
#
#     return total
#
#
# print(sum_it(1, 2, 3, 4, 5, 6, limit=3))

# ******************************************************************************

#
# def counts_words(*args, ignore_case: bool = True) -> str:
#     """
#     This Function Get List With Words And Count Quality. Returns The Most Frequent Word.
#     :param args: List With Words.
#     :param ignore_case: If True Ignore Upper Letters.
#     :return: The Most Frequent Word.
#     """
#
#     words_dict = {}
#     for arg in args:
#         arg = arg.lower() if ignore_case else arg
#         words_dict[arg] = words_dict.get(arg, 0) + 1
#
#     for key, count in words_dict.items():
#         if count == max(words_dict.values()):
#             return f"{key.capitalize()} - {words_dict[key]}"
#
#
# print(counts_words('Ala', 'Ola', 'ala', 'olo', 'ola', 'ala', 'olo', 'olo', 'Ala'))
# print(counts_words('Ala', 'Ola', 'ala', 'olo', 'ola', 'ala', 'olo', 'olo', 'Ala', ignore_case=False))

# ******************************************************************************


