from protocol.problem_5_p_12 import Problem5P12
import random

"""
THINGS TO NOTE ABOUT THIS PROBLEM

Problem 5.12var1 was not coded since there is no coding really involved. It is answered here:
https://www.quora.com/The-rand-function-in-the-standard-C-library-returns-a-uniformly-random-number-in-0-RAND_MAX-1-Does-rand-mod-n-generate-a-number-uniformly-distributed-0-n-1
"""


class Problem5P12Vlad(Problem5P12):
    def random_sampling(self, distinct_elem_list, size):
        self.per_element_random_sampling(distinct_elem_list, size)

    # the random list of size elements is the last size elements of distinct_elem_list
    def per_element_random_sampling(self, distinct_elem_list, size):
        if size <= len(distinct_elem_list):
            for elements_done in range(size):
                last_undone_elem = len(distinct_elem_list) - 1 - elements_done
                selected_elem = random.randint(0, last_undone_elem)
                distinct_elem_list[last_undone_elem], distinct_elem_list[selected_elem] = \
                    distinct_elem_list[selected_elem], distinct_elem_list[last_undone_elem]
        else:
            # if size is > len(distinct_elem_list)/2 then it is faster to select elements not to include and place them
            # at the beginning of the list
            for elements_done in range(len(distinct_elem_list) - size):
                first_undone_elem = elements_done
                selected_elem = random.randint(first_undone_elem, len(distinct_elem_list) - 1)
                distinct_elem_list[first_undone_elem], distinct_elem_list[selected_elem] = \
                    distinct_elem_list[selected_elem], distinct_elem_list[first_undone_elem]
