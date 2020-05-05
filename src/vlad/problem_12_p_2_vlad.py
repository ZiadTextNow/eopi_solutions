from protocol.problem_12_p_2 import Problem12P2
import collections

"""
THINGS TO NOTE ABOUT THIS PROBLEM

I swear the pythonic was is slower since it creates a dict for both every time
"""


class Problem12P2Vlad(Problem12P2):
    def is_anonymous_letter_constructable(self, anonymous_letter, text_for_magazine):
        # return self.pythonic_way(anonymous_letter, text_for_magazine)
        return self.fastest_solution(anonymous_letter, text_for_magazine)

    def pythonic_way(self, anonymous_letter, text_for_magazine):
        letter_count = collections.Counter(anonymous_letter)
        magazine_count = collections.Counter(text_for_magazine)
        return not (letter_count - magazine_count)   # this is because Counter only keeps positive counts

    def fastest_solution(self, anonymous_letter, text_for_magazine):
        letter_count = collections.Counter(anonymous_letter)

        for c in text_for_magazine:
            if c in letter_count:
                letter_count[c] -= 1   # decrement letters needed
                if letter_count[c] == 0:
                    del letter_count[c]   # delete that key since no more that letter is needed
                    if not letter_count:
                        return True   # if no more letters are needed at all, success and return True!!!

        return not letter_count
