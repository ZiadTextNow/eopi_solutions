from protocol.problem_5_p_6_var1 import Problem5P6Var1
import sys


class Problem5P6Var1Ziad(Problem5P6Var1):
    def find_longest_equal_sublist(self, int_list):
        return self.naive(int_list)

    # Iterate over int_list, maintaining a count for the longest sub array so far.
    # time: O(n)
    # space: O(1)
    def naive(self, int_list):
        # the smallest a sub array can be is a single element, so initialize with 1
        max_sub_array_length_so_far, current_sub_array_length = 1, 1

        for i in range(len(int_list) - 1):
            if int_list[i] == int_list[i + 1]:
                current_sub_array_length += 1
            else:
                current_sub_array_length = 1

            max_sub_array_length_so_far = max(max_sub_array_length_so_far, current_sub_array_length)

        return max_sub_array_length_so_far

