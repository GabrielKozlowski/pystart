

# class Circle:

#     def __init__(self, radius:int) -> None:
#         self.radius = radius

    
#     def perimeter(self):
#         return (2 * 3.14 * self.radius)
    

#     def field(self):
#         return (3.14 * (self.radius ** 2))
    


# def test_circle_perimeter():
#     # Give:
#     radius = 4

#     # When:
#     result = Circle(radius)

#     # Than:
#     assert result.perimeter() == 25.12


# def test_circle_field():
#     # Give:
#     radius = 4

#     # When:
#     result = Circle(radius)

#     # Than:
#     assert result.field() == 50.24


# if __name__ == '__main__':
#     value = Circle(int(input('Enter value of circle radius: ')))
#     print(f"Perimeter of circle: {value.perimeter()}\nField of circle: {value.field()}")

# ########################################################################################################################


# class Car:

    

#     def __init__(self, name:str, price:float, vmax:int):
#         self.name = name
#         self.price = price
#         self.vmax = vmax


# cars_list = []

# car1 = Car('Bmw', 33.234, 170)
# car2 = Car('Audi', 35.223, 190)

# cars_list.append(car1)
# cars_list.append(car2)

# for car in cars_list:
#     print(f"Car name: {car.name}, price: {car.price}, v-max: {car.vmax}")

#################################################################################################################
