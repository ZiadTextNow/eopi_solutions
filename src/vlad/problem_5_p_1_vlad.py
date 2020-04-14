from protocol.problem_5_p_1 import Problem5P1

"""
THINGS TO NOTE ABOUT THIS PROBLEM

"""


class Problem5P1Vlad(Problem5P1):
    def dutch_flag_partition(self, pivot_index, unpartitioned_list):
        pivot = unpartitioned_list[pivot_index]
        # self.two_pass_dutch_flag_partition(pivot, unpartitioned_list)
        self.one_pass_dutch_flag_partition(pivot, unpartitioned_list)

    def two_pass_dutch_flag_partition(self, pivot, unpartitioned_list):
        low_idx = 0   # leftmost value that is > pivot
        for index in range(len(unpartitioned_list)):
            if unpartitioned_list[index] < pivot:
                unpartitioned_list[low_idx], unpartitioned_list[index] = unpartitioned_list[index], unpartitioned_list[low_idx]
                low_idx += 1

        high_idx = len(unpartitioned_list) - 1   # rightmost unknown value. Values to the right are > pivot
        for index in reversed(range(len(unpartitioned_list))):
            if unpartitioned_list[index] > pivot:
                unpartitioned_list[high_idx], unpartitioned_list[index] = unpartitioned_list[index], unpartitioned_list[high_idx]
                high_idx -= 1

    # @staticmethod
    def one_pass_dutch_flag_partition(self, pivot, unpartitioned_list):
        low_idx = 0   # leftmost value that is == pivot
        unknown_idx = 0   # idx of the leftmost unknown value
        high_idx = len(unpartitioned_list) - 1   # rightmost unknown value. Values to the right are > pivot
        """"
        Important to note for my solution unlike books I must put <= instead of < here since the book decrements 
        high_idx before setting values while I do it after. In my case both high_idx and unknown_idx point at unknown 
        values
        """
        while unknown_idx <= high_idx:
            if unpartitioned_list[unknown_idx] < pivot:
                unpartitioned_list[low_idx], unpartitioned_list[unknown_idx] = unpartitioned_list[unknown_idx], unpartitioned_list[low_idx]
                low_idx += 1
                unknown_idx += 1
            elif unpartitioned_list[unknown_idx] == pivot:
                unknown_idx += 1
            elif unpartitioned_list[unknown_idx] > pivot:
                unpartitioned_list[high_idx], unpartitioned_list[unknown_idx] = unpartitioned_list[unknown_idx], unpartitioned_list[high_idx]
                high_idx -= 1

