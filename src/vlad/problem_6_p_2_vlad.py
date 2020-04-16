from protocol.problem_6_p_2 import Problem6P2
import string

"""
THINGS TO NOTE ABOUT THIS PROBLEM

string.digits and string.hexdigits is an absolute beauty!!!
"""


class Problem6P2Vlad(Problem6P2):
    def base_conversion(self, str_b1, b1, b2):
        return self.convert_via_base_ten(str_b1, b1, b2)

    def convert_via_base_ten(self, str_b1, b1, b2):
        int_b10 = 0
        for digit in str_b1[str_b1[0] == '-':]:   # converting str_b1 to an int of base 10
            int_of_char = string.hexdigits.upper().index(digit)
            int_b10 = int_b10 * b1 + int_of_char
        int_b10 *= (-1 if str_b1[0] == '-' else 1)

        str_b2_list = []
        is_negative = False
        if int_b10 < 0:
            is_negative, int_b10 = True, -int_b10
        while int_b10:   # converting int_b10 to a string of base b2
            # ascii_idx = ord('0') + int_b10 % b2 if int_b10 % b2 < 10 else ord('A') + (int_b10 % b2 - 10)
            # str_b2_list.append(chr(ascii_idx))
            # above was my way of doing what is done below by the book and is better so I used it!
            str_b2_list.append(string.hexdigits[int_b10 % b2].upper())
            int_b10 //= b2
        str_b2 = ('-' if is_negative else '') + ''.join(reversed(str_b2_list))
        return str_b2


