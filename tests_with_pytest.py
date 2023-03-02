
def count_letters(text: str, start: str = '(', stop: str = ')') -> int:
    """
    This Function Count Letters Between Brackets
    :param text: String To Check
    :param start: Bracket When Function Starts Count
    :param stop: Bracket When Function Stops Count
    :return: Number Of Letters In Between Brackets
    """
    total = 0
    for word in text.split(' '):
        if word.startswith(start) and word.endswith(stop):
            total += len(word) - 2

    return total


def test_count_letters_in_brackets():
    # Given:
    string_test = 'I (love) python'
    bad_string = 'i <love> python'
    only_string = 'i love python'

    # When:
    result = count_letters(string_test)
    result1 = count_letters(bad_string, start='<', stop='>')
    result2 = count_letters(only_string)

    # Than:
    assert result == 4
    assert result1 == 4
    assert result2 == 0

######################################################################################


def test_common_divisor_by_2_numbers():
    # Given:
    a = 20
    b = 44

    # When:
    result = common_divisor(a, b)

    # Than:
    assert result == 4


def common_divisor(numb1: int, numb2: int) -> int:
    """
    This Function Search For Common Divisor From Two Numbers
    :param numb1: First Number
    :param numb2: Second Number
    :return: Largest Number Of Common Divisor
    """

    if numb2 == 0:
        return numb1

    return common_divisor(numb2, (numb1 % numb2))


def test_divide_numbers_by_number():
    # Given:
    a = 5
    b = 25
    c = 5

    # When:
    result = divide_numbers_by_number(a, b, c)

    # Than:
    assert result == [5, 10, 15, 20, 25]


def divide_numbers_by_number(numb1: int = 0, numb2: int = 0, step: int = 1) -> list:
    """
    This Function Count How Many Numbers Are Divided By Number In Range Numb1 - Numb2
    :param numb1: Smallest Number In Range
    :param numb2: Largest Number In Range
    :param step: Number For Step In Divide Range
    :return: List With Numbers Divided By Number In Range
    """
    output = []
    numbers = range(numb1, numb2 + 1)
    for n in numbers:
        if n % step == 0:
            output.append(n)

    return output


def test_check_string_for_appropriate_letters():
    # Given:
    text = 'ala ma kota i kot ma ale'
    # When:
    result = check_string_for_appropriate_letters(text)
    # Than:
    assert result == ['ma', 'kota', 'ma']


def check_string_for_appropriate_letters(text: str) -> list:
    """
    This Function Search For Word Which Starts On Consonant And Ends On Wolves
    :param text: String To Check
    :return: List With Correct Words
    """
    wolves ='aąeęoóuiy'
    output = []
    for word in text.split(' '):
        if word[0] not in wolves and word[-1] in wolves:
            output.append(word)


    return output

##########################################################################################


from math import ceil


def get_divisor(number: int) -> list:
    """
    This Function Get Number And Return All Divided Numbers
    :param number: Number To Calculate
    :return: All Numbers Are Divided By Number
    """
    output = []
    for n in range(2, ceil(number / 2) + 1):
        if number % n == 0:
            output.append(n)
    output.append(number)

    return output


def gdc(number1: int, number2: int) -> set:
    """
    This Function Return Common Divider Of Number1 And Number2
    :param number1: First Number
    :param number2: Second Number
    :return: The Largest Common Divider Number In Set
    """
    divisor1 = set(get_divisor(number1))
    divisor2 = set(get_divisor(number2))

    same_divisors = divisor1 & divisor2

    return max(same_divisors) if len(same_divisors) > 0 else None


def test_get_divisor():
    assert get_divisor(20) == [2, 4, 5, 10, 20]
    assert get_divisor(7) == [7]


def test_gdc():
    assert gdc(20, 30) == 10
    assert gdc(6, 12) == 6
    assert gdc(7, 30) is None

#####################################################################################


def get_divisors(start: int, stop: int, step: int) -> list:
    """
    This Function Get Numbers Range And Divided It By Number
    :param start: First Number Of Range
    :param stop: Last Number Of Range
    :param step: Number For Divide Numbers In Range
    :return: List With All Divisor Numbers
    """
    output = []
    for number in range(start, stop + 1):
        if number % step == 0:
            output.append(number)

    return output


def test_get_divisors():
    assert isinstance(get_divisors(2, 12, 2), list)
    assert get_divisors(2, 12, 2) == [2, 4, 6, 8, 10, 12]
    assert get_divisors(3, 12, 2) == [4, 6, 8, 10, 12]
    assert get_divisors(2, 4, 20) == []


################################################################################


def get_string(text: str) -> list:
    """
    THis Function Checks Text For Words Start With Consonant And Ends Withe Wolves
    :param text: String With Words To Check
    :return: List With All Correct Words
    """

    wolves = 'aąeęoóuiy'
    output = [word for word in text.split(' ') if word[0].lower() not in wolves and word[-1].lower() in wolves]

    return output


def test_get_string():
    assert get_string('Ala Ma Kota') == ['Ma', 'Kota']
    assert get_string('Ala ma kota') == ['ma', 'kota']
    assert get_string('Ala MA kotA') == ['MA', 'kotA']
    assert get_string('Ala mam kot') == []

