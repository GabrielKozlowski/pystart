
# # >>>>>>>>>>>>>>> First task to do. <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# # Create Function And Test For This Function.

def group_them(**kwargs) -> str:
    """
    This Function Get Kwargs And Return Key As Title And Value As Lower
    :param kwargs: Kwargs
    :return: String In New Line
    """
    output = []
    for key, value in kwargs.items():
        output.append(f"{key.title()} is {value}")

    return '\n'.join(output)

def test_group_them():
    assert group_them() == ''
    assert group_them(python='super', php='almost super') == 'Python is super\nPhp is almost super'


print(group_them(python='super', php='almost super'))

# # >>>>>>>>>>>>>>> Second task to do. <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# # Create Package Finances With Modul 'Budget' and 'Ecommerce' With Defs


# # >>>>>>>>>>>>>>> Third task to do. <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# # Create Functon And Test. Count Word In String

def count_word_in_string(text: str, searched_word: str, capitalization: bool = True) -> int:
    """
    This Function Counts Word In String
    :param text: String For Check
    :param searched_word: Word For Searching In String
    :param capitalization: If Is False, it Isn't Matter Size Of First Letter. Default True
    :return: Number Of Word
    """
    total = 0
    for word in text.split(' '):
        if not capitalization:
            word = word.lower()
            searched_word = searched_word.lower()

        if word == searched_word:
            total += 1

    return total


def test_count_word_in_string():
    assert count_word_in_string('Python and Python and python', 'Python') == 2
    assert count_word_in_string('Python and Python and python', 'Python', capitalization=False) == 3
    assert count_word_in_string('Python and Python and python', 'Django') == 0
    assert count_word_in_string('Python and Python and python', 'Django', capitalization=False) == 0

# # >>>>>>>>>>>>>>> Fourth task to do. <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# # Create Function. Check If Password Is Correct And Return True Or False

def check_pesel(password: int = 0) -> bool:
    """
    This Function Check If Password Is Correct And Return Bool
    :param password: String To Check
    :return: Bool Value
    """
    control_numbers = 13791379131
    if len(str(password)) != 11:
        return False

    pesel_sum = 0
    for number, control in zip(str(password), str(control_numbers)):
        pesel_sum += int(number) * int(control)

    return True if str(pesel_sum).endswith('0') else False


def test_check_pesel():
    assert check_pesel(51062488907) is True
    assert check_pesel(510624889070) is False
    assert check_pesel(51062488908) is False
    assert check_pesel() is False



# # >>>>>>>>>>>>>>> Fifth and Sixth task to do. <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# # Create Function. Count BMI Withe Height And Weight.
# # Create Function. Check BMI Result With Tabel ANd Return Information

def count_bmi(height: float, weight: float) -> float:
    """
    This Function Calculate BMI Value From Weight And Weight
    :param height: Value In Float
    :param weight: Value In Float
    :return: Float Value
    """
    if weight is None and height is None:
        return None

    return float(f"{weight / (height / 100) ** 2:.2f}")


def test_count_bmi():
    assert count_bmi(187.2, 108.3) == 30.90


def print_info_of_bmi(bmi: float = 0) -> str:
    """
    This Function Return Text Based On BMI Value
    :param bmi: Value Of Bmi
    :return: String With Information Of Bmi
    """
    if bmi == 0:
        return None


    if bmi < 16:
        result = "Starvation"
    elif 16 <= bmi <= 16.99:
        result = "Emaciation"
    elif 17 <= bmi <= 18.49:
        result = "Underweight"
    elif 18.5 <= bmi <= 24.99:
        result = "Correct Value"
    elif 25 <= bmi <= 29.99:
        result = "Overweight"
    elif 30 <= bmi <= 34.99:
        result = "I Degree Obesity"
    elif 35 <= bmi <= 39.99:
        result = "2nd Degree Obesity"
    else:
        result = "Extreme Obesity"

    return f"Your Result Of {bmi:.2f} Bmi = {result}."

print(print_info_of_bmi(count_bmi(187.0, 87.40)))

def test_print_info_of_bmi():
    assert print_info_of_bmi(15.12) == "Your Result Of 15.12 Bmi = Starvation."
    assert print_info_of_bmi(16.30) == "Your Result Of 16.30 Bmi = Emaciation."
    assert print_info_of_bmi(18.01) == "Your Result Of 18.01 Bmi = Underweight."
    assert print_info_of_bmi(19.34) == "Your Result Of 19.34 Bmi = Correct Value."
    assert print_info_of_bmi(25.50) == "Your Result Of 25.50 Bmi = Overweight."
    assert print_info_of_bmi(31.12) == "Your Result Of 31.12 Bmi = I Degree Obesity."
    assert print_info_of_bmi(35.22) == "Your Result Of 35.22 Bmi = 2nd Degree Obesity."
    assert print_info_of_bmi(41.00) == "Your Result Of 41.00 Bmi = Extreme Obesity."
    assert print_info_of_bmi() is None