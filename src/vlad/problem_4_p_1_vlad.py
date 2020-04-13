from protocol.problem_4_p_1 import Problem4P1

"""
THINGS TO NOTE ABOUT THIS PROBLEM

x & (x-1) = x with lowest set bit set to zero is super cool!
You can cache to save time if calculation is to be done many times
Can you use XORs associative and commutative properties to perform operations in any order and size
"""


class Problem4P1Vlad(Problem4P1):
    def get_parity(self, num):
        return self.cache_parity(num)

    """
    Did these myself but realized I could have just XORed right away instead of making a parity function
    """
    def count_bits(self, x):
        num_bits = 0
        while x:
            num_bits += x & 1
            x >>= 1
        return num_bits

    def fast_count_bits(self, x):
        # Using the trick that x & (x - 1) = x with least significant bit set to 0
        num_bits = 0
        while x:
            num_bits += 1
            x &= x - 1
        return num_bits

    def parity(self, x, count_bits_function=count_bits):
        num_bits = count_bits_function(x)
        parity = num_bits % 2
        return parity

    """
    Lookup table for 4-bit parity
    """
    four_bit_LUT = {
        0b0000: 0,
        0b0001: 1,
        0b0010: 1,
        0b0011: 0,
        0b0100: 1,
        0b0101: 0,
        0b0110: 0,
        0b0111: 1,
        0b1000: 1,
        0b1001: 0,
        0b1010: 0,
        0b1011: 1,
        0b1100: 0,
        0b1101: 1,
        0b1110: 1,
        0b1111: 0
    }

    def cache_parity(self, x):
        mask = 0b1111
        parity = 0
        while x:
            parity ^= self.four_bit_LUT[(x & mask)]
            x >>= 4
        return parity

    """
    This assumes x is at max 64 bits!
    """
    def xor_parity(self, x):
        x ^= x >> 32
        x ^= x >> 16
        x ^= x >> 8
        x ^= x >> 4
        x ^= x >> 2
        x ^= x >> 1
        return x & 1
