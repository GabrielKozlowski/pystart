
# # >>>>>>>>>>>>>>> First task to do. <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
def group_them(wall: str='red', tomato: str='red', light: str='yellow', lemon: str='yellow', grass: str='green') -> str:
    """
    This Function Get Colors In String And Return Result
    :param wall: Color For Wall
    :param tomato: Color For Tomato
    :param light: Color For Light
    :param lemon: Color For Lemon
    :param grass: Color For Grass
    :return: String With Added Values
    """
    return f"Wall is {wall} \nTomato is {tomato} \nLight is {light} \nLemon is {lemon} \nGrass is {grass}"


def test_group_them():
    assert group_them() == "Wall is red \nTomato is red \nLight is yellow \nLemon is yellow \nGrass is green"
    assert group_them(wall='black', grass='white') == "Wall is black \nTomato is red \nLight is yellow " \
                                                      "\nLemon is yellow \nGrass is white"
    assert group_them(tomato='green', lemon='blue') == "Wall is red \nTomato is green \nLight is yellow " \
                                                       "\nLemon is blue \nGrass is green"
    assert group_them(light='orange') == "Wall is red \nTomato is red \nLight is orange \nLemon is yellow " \
                                         "\nGrass is green"

# # >>>>>>>>>>>>>>> Second task to do. <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# # Create Package Finances With Modul 'Budget' and 'Ecommerce' With Defs


# # >>>>>>>>>>>>>>> Third task to do. <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<


# # >>>>>>>>>>>>>>> Fourth task to do. <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<


# # >>>>>>>>>>>>>>> Fifth task to do. <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<


# # >>>>>>>>>>>>>>> Sixth task to do. <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

