from protocol.problem_4_p_7 import Problem4P7

"""
THINGS TO NOTE ABOUT THIS PROBLEM

Powers of numbers can be simplified by breaking them up into products of powers of 2. 
For instance 2.0 ** 7 = 2**4 * 2**2 * 2**1 = (2**2)**2 * 2**2 * 2**1
"""

class Problem4P7Vlad(Problem4P7):
    def x_to_the_y(self, x, y):
        result, power = 1.0, y
        if y < 0:
            x, power = 1.0 / x, -power   # Since x ** -y == 1/x ** y
        while power:   # Go through all set bits of power
            if power & 1:   # If this bit of power is set multiply to result the running product on x
                result *= x
            x *= x   # Running product of product of product etc... of x
            power >>= 1
        return result

