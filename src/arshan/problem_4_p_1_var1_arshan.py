from protocol.problem_4_p_1_var1 import Problem4P1Var1


class Problem4P1Var1Arshan(Problem4P1Var1):
    def right_prop_rightmost_bit(self, num):
        return num if num <= 0 else num | (num - 1)

    def mod_power_two(self, num, power_two):
        return num & (power_two - 1)

    def is_power_two(self, num):
        return False if num <= 0 else (num & (num - 1)) == 0
