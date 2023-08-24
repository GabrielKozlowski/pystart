#
#
# from math import ceil
#
# walls = int(input("Ile jest ścian do pomalowania? "))
# print("Wszystklie wartości podawaj w metrach np 3.2")
# print("Jeśli chcesz przyjąć poprzednią wartość to wciśnij enter.")
# current_height = 3
# area_to_paint = 0
#
#
# for counter in range(walls):
#     width = float(input(f"Podaj mi szerokość ściany {counter + 1}:"))
#     height = input(f"Podaj mi wysokość ściany {counter + 1}:")
#
#     if height == '':
#         height = current_height
#     else:
#         current_height = float(height)
#     area_to_paint += float(height) * width
#
# print(f"Powierzchnia do pomalowania wynosi: {area_to_paint}mkw")
#
# layers_of_base = int(input("Ile warstw gruntu? "))
# layers_of_paint = int(input("Ile warstw farby? "))
#
# liters_of_base = ceil(area_to_paint * layers_of_base / 5)
# liters_of_paint = ceil(area_to_paint * layers_of_paint / 13)
#
# print(f"Potrzebujesz {liters_of_base} litrów gruntu.")
# print(f"Potrzebujesz {liters_of_paint} litrów farby.")
#
