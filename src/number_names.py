def convert_single_digit(integer_in: int) -> str:
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
    if integer_in < 100:
        return convert_two_digit(integer_in)
    hundreds = integer_in // 100
    leftovers = integer_in - hundreds * 100
    hundred_string = convert_single_digit(hundreds)
    leftovers_string = " and " + (convert_two_digit(leftovers)) if leftovers != 0 else ""
    final_string = f"{hundred_string} hundred{leftovers_string}"
    return final_string


def convert_number(integer_in: int) -> str:
    if integer_in < 1_000:
        return convert_three_digit(integer_in)
    elif integer_in < 1_000_000:
        thousands = integer_in // 1_000
        leftovers = integer_in - thousands * 1_000
        thousands_string = f"{convert_three_digit(thousands)} thousand"
        connection = " and " if leftovers < 100 else ", "
        leftovers_string = f"{connection}{convert_three_digit(leftovers)}" if leftovers != 0 else ""
        return thousands_string + leftovers_string
