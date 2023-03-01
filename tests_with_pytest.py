
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
