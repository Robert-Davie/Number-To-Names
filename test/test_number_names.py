from src import number_names


def test_11():
    assert number_names.convert_two_digit(11) == "eleven"


def test_20():
    assert number_names.convert_two_digit(20) == "twenty"


def test_99():
    assert number_names.convert_two_digit(99) == "ninety-nine"


def test_100():
    assert number_names.convert_three_digit(100) == "one hundred"


def test_101():
    assert number_names.convert_three_digit(101) == "one hundred and one"


def test_777():
    assert number_names.convert_three_digit(777) == "seven hundred and seventy-seven"


def test_210():
    assert number_names.convert_three_digit(210) == "two hundred and ten"


def test_1_001():
    assert number_names.convert_number(1_001) == "one thousand and one"


def test_10_001():
    assert number_names.convert_number(10_001) == "ten thousand and one"


def test_123_456():
    target_string = "one hundred and twenty-three thousand, four hundred and fifty-six"
    assert number_names.convert_number(123456) == target_string
