from protocol.problem_4_p_1 import Problem4P1


class Problem4P1Arshan(Problem4P1):
    def get_parity(self, num):
        return self.use_what_uve_seen_so_far({}, num)
        return self.set_least_bit(num)


    """
    I came up with this myself.
    """
    def brute_force(self, num):
        parity = 0
        while num:
            parity ^= (num & 1)
            num >>= 1
        return parity

    """
    This BLEW my mind. Very cool.
    """
    def set_least_bit(self, num):
        parity = 0
        while num:
            parity ^= 1
            num = num & (num - 1)
        return parity

    def _get_length(self, num):
        return len(bin(num)) - 2

    """
    This is some weird binary divide-and-conquer dynamic programming bullshit I
    came up with, works tho. 
    """
    def use_what_uve_seen_so_far(self, lookup, num):
        lookup = lookup or {
            1: {
                '1': 1,
                '0': 0
            }
        }
        num_length = self._get_length(num)
        parity = 0
        while num:
            lengths_sorted = sorted(lookup.keys(), reverse=True)
            biggest_length = lengths_sorted[0]
            if num_length > biggest_length:
                mask = (1 << biggest_length) - 1
                chunk = num & mask
                parity ^= self.use_what_uve_seen_so_far(lookup, chunk)
                num >>= biggest_length
            if num in lookup[num_length]:
                return lookup[num_length][num]
            first_half = num & ((1 << (num_length >> 1)) - 1)
            second_half = num >> (num_length >> 1)
            first_parity = self.use_what_uve_seen_so_far(lookup,
                                                         first_half)
            second_parity = self.use_what_uve_seen_so_far(lookup,
                                                         second_half)
            parity = first_parity ^ second_parity
            lookup[num_length][num] = parity
            return parity
        return parity
