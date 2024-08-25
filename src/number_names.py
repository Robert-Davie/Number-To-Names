def convert_single_digit(integer_in: int) -> str:
    """
    convert single digit to its english name
    :param integer_in: integer to be converted
    :return: english name of the integer
    """
    single_digit_dictionary = {
        0: "zero",
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
    }
    return single_digit_dictionary[integer_in]


def convert_two_digit(integer_in: int) -> str:
    """
    convert two digit integer to its english name
    :param integer_in: the two digit integer
    :return: the english name of the two digit integer
    """
    if integer_in < 10:
        return convert_single_digit(integer_in)
    if integer_in < 20:
        small_double_digit_dictionary = {
            10: "ten",
            11: "eleven",
            12: "twelve",
            13: "thirteen",
            14: "fourteen",
            15: "fifteen",
            16: "sixteen",
            17: "seventeen",
            18: "eighteen",
            19: "nineteen",
        }
        return small_double_digit_dictionary[integer_in]
    double_digit_dictionary = {
        20: "twenty",
        30: "thirty",
        40: "forty",
        50: "fifty",
        60: "sixty",
        70: "seventy",
        80: "eighty",
        90: "ninety",
    }
    ones = integer_in % 10
    tens = integer_in - ones
    one_string = ("-" + convert_single_digit(ones)) if ones != 0 else ""
    final_string = double_digit_dictionary[tens] + one_string
    return final_string


def convert_three_digit(integer_in: int) -> str:
    """
    convert a three digit integer to its english name
    :param integer_in: the three digit integer
    :return: the english name of the three digit integer
    """
    if integer_in < 100:
        return convert_two_digit(integer_in)
    hundreds = integer_in // 100
    leftovers = integer_in - hundreds * 100
    hundred_string = convert_single_digit(hundreds)
    leftovers_string = (
        " and " + (convert_two_digit(leftovers)) if leftovers != 0 else ""
    )
    final_string = f"{hundred_string} hundred{leftovers_string}"
    return final_string


def get_triples(integer_in: int) -> list[int]:
    """
    get the list of triples of digits that make up the integer
    example:
    1,234,567 -> [1, 234, 567]
    :param integer_in: the integer to create the list of triples from
    :return: the list of triples
    """
    res = []
    temp = integer_in
    while temp >= 1:
        res.append(temp % 1000)
        temp = temp // 1000
    return res[::-1]


def get_triples_with_positions(integer_in: int) -> list[(int, int)]:
    """
    gets the triples of digits of an integer with their relative size
    examples:
    \n1,234,567 -> [(2, 1), (1, 234), (0, 567)]
    \n1,000,000,000 -> [(3, 1), (2, 0), (1, 0), (0, 0)]
    :param integer_in: integer to create list from
    :return: pairs of values in a list where pair[0] represent the relative size and pair[1] represents the triple
    """
    triples = get_triples(integer_in)
    res = [((len(triples) - 1) - i, j) for i, j in enumerate(triples)]
    return res


def remove_trailing_punctuation(string_in: str) -> str:
    """
    removes all trailing punctuation from a given string
    :param string_in: the string to be improved
    :return: the improved version of the string
    """
    letters = "abcdefghijklmnopqrstuvqxyz"
    letters = letters + letters.upper()
    non_punctuation = letters + "0123456789"
    if len(string_in) == 0:
        return ""
    temp = string_in
    while len(temp) > 0 and temp[-1] not in non_punctuation:
        temp = temp[:-1]
    return temp


def convert_integer_to_english(integer_in: int) -> str:
    """
    converts an integer to its english name (British format)
    e.g. 1234 -> one thousand, two hundred and thirty-four
    :param integer_in: the integer to be converted
    :return: the english name of the integer
    """
    answer_string = ""
    if integer_in < 0:
        return "negative " + convert_integer_to_english(-1 * integer_in)
    if integer_in == 0:
        return "zero"
    if integer_in < 1000:
        return convert_three_digit(integer_in)
    triple_names = {
        0: "",
        1: "thousand",
        2: "million",
        3: "billion",
        4: "trillion",
        5: "quadrillion",
        6: "quintillion",
        7: "sextillion",
    }
    triples = get_triples_with_positions(integer_in)
    for triple_size, triple in triples:
        if triple == 0:
            continue
        if triple_size == 0:
            if triple < 100:
                answer_string = remove_trailing_punctuation(answer_string) + " "
                answer_string += f"and {convert_two_digit(triple)}"
            else:
                answer_string += f"{convert_three_digit(triple)}"
        else:
            answer_string += (
                f"{convert_three_digit(triple)} {triple_names[triple_size]}, "
            )
    answer_string = remove_trailing_punctuation(answer_string)
    return answer_string
