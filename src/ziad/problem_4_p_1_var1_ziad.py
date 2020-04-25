from protocol.problem_4_p_1_var1 import Problem4P1Var1

class Problem4P1ZiadVar1(Problem4P1Var1):
    def right_prop_rightmost_bit(self, num):
        # or any digit after the right-most 1 with 1 to make all the 0s into 1s
        # the number we are looking for is num - 1, since all the digits left of the rightmost
        # 1 will be 0 in both and the rightmost bits will all be set
        return 0 if num == 0 else (num | num - 1)

    def mod_power_two(self, num, power_two):
        # this is a trick with binary arithmetic. To see the pattern, write out the binary
        # representation of both num and power_two to realize that the (n mod d) is simply
        # equal to n's bits that are to the right of its MSB. So we just AND num with
        # power_two - 1
        return num & (power_two - 1)

    def is_power_two(self, num):
        return True if not (num & (num - 1)) else False