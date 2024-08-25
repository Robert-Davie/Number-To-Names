from src import number_names
import pytest


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
    assert number_names.convert_integer_to_english(1_001) == "one thousand and one"


def test_10_001():
    assert number_names.convert_integer_to_english(10_001) == "ten thousand and one"


def test_123_456():
    target_string = "one hundred and twenty-three thousand, four hundred and fifty-six"
    assert number_names.convert_integer_to_english(123456) == target_string


def test_1_001_001():
    target_string = "one million, one thousand and one"
    assert number_names.convert_integer_to_english(1_001_001) == target_string


def test_trillion():
    assert number_names.convert_integer_to_english(10**12) == "one trillion"


def test_get_triples():
    assert number_names.get_triples(123_000_001) == [123, 0, 1]


def test_get_triples_2():
    assert number_names.get_triples(12_000_000) == [12, 0, 0]


def test_get_triples_3():
    assert number_names.get_triples(1_234_567) == [1, 234, 567]


def test_get_triples_with_positions():
    assert number_names.get_triples_with_positions(1_234_567) == [
        (2, 1),
        (1, 234),
        (0, 567),
    ]


def test_removing_trailing_non_digits():
    assert number_names.remove_trailing_punctuation("23490.,  .,.") == "23490"


def test_negative_1():
    assert number_names.convert_integer_to_english(-1) == "negative one"
