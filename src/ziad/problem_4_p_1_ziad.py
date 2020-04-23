from protocol.problem_4_p_1 import Problem4P1

class Problem4P1Ziad(Problem4P1):
    """
        The parity of a word is 1 if the number of 1s in the word
        is off, and 0 otherwise.
        
        e.g. parity(1) is 1
             parity(101) is 0
             parity(10101001010) is 1 
             parity(000000) is 0
    """
    def get_parity(self, num):
        return self.naive(num)
        return self.recursive(num, 0)
        return self.bit_manipulation_with_XOR(num)

    """
    Helper Function
    """
    def __is_odd(self, x):
        if x % 2 == 1:
            return 1
        return 0

    # """
    # NOTE: This will BLOW the stack if we use large numbers :)
    #
    # Recursive solution (i.e. Divide & Conquer):
    #     Look at the current bit, and infer its parity, then divide the number by 2.
    #     Stop when you reach the base case, i.e. when the word is "1".
    #
    # time: O(n) where n is the # of bits used to represent num
    # """
    # def recursive(self, num, number_of_ones_so_far):
    #     # base case
    #     if num == 1:
    #         return self.__is_odd(number_of_ones_so_far + 1)
    #
    #     # recurrence relation
    #     # The trick here is to realize that if we have a "1" in the LSB,
    #     # it must mean that the number is odd
    #     number_of_ones_so_far = (number_of_ones_so_far + 1) if self.__is_odd(num) else number_of_ones_so_far
    #     return self.recursive(num / 2, number_of_ones_so_far)

    """
    Bit Manipulation Solution:
        Check the LSB in the word by ANDing it with 1, then rotate it out.
        Repeat until num is 0.
        Time: O(n)
        Space: O(m) where m is the number of bits in num
    """
    def naive(self, num):
        ones = 0

        while num:
            ones += 1 if (num & 1 == 1) else 0
            num >>= 1

        return ones % 2 == 1

    '''
    This is a pretty well-known solution with the advantage of being the
    most efficient solution (O(log(n) runtime) but with the limitation of only
    working with 64-bit numbers or smaller.
    '''
    def bit_manipulation_with_XOR(self, num):
        num ^= num >> 32
        num ^= num >> 16
        num ^= num >> 8
        num ^= num >> 4
        num ^= num >> 2
        num ^= num >> 1
        return num & 1

 #TODO: Cache-based implementation








