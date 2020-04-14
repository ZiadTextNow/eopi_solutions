from protocol.problem_4_p_1_var1 import Problem4P1Var1

"""
THINGS TO NOTE ABOUT THIS PROBLEM

x & (x-1) = x with lowest set bit set to zero idea can be used for all problems below 
"""


class Problem4P1Var1Vlad(Problem4P1Var1):
    # Ex: x = 01010000, returns 01010000 | 01001111
    def right_prop_rightmost_bit(self, num):
        # If num == 0 return 0 since num - 1 will overflow
        if num:
            return num | (num - 1)
        return 0

    # Ex: x = 01001101(77), mod = 01000000(64)
    # returns 01001101 & 00111111
    def mod_power_two(self, num, power_two):
        return num & (power_two - 1)

    # Ex: x = 01000000, returns not(01000000 & 00111111)
    def is_power_two(self, num):
        if num:
            return not (num & (num - 1))
        return False

