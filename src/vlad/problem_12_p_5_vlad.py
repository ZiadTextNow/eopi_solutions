from protocol.problem_12_p_5 import Problem12P5
import collections

"""
THINGS TO NOTE ABOUT THIS PROBLEM

"""


class Problem12P5Vlad(Problem12P5):
    def nearest_repeated_words(self, word_list):
        return self.using_hash_map(word_list)

    def using_hash_map(self, word_list):
        repeated_word = None
        smallest_distance = float('inf')
        word_idx_dict = {}

        for index, word in enumerate(word_list):
            if word_idx_dict.get(word) and index - word_idx_dict[word] < smallest_distance:
                    smallest_distance = index - word_idx_dict[word]
                    repeated_word = word
            word_idx_dict[word] = index

        return repeated_word, smallest_distance if repeated_word else None
