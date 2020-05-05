from protocol.problem_13_p_1 import Problem13P1
import collections

"""
THINGS TO NOTE ABOUT THIS PROBLEM

"""


class Problem13P1Vlad(Problem13P1):
    def intersection_of_two_sorted_lists(self, sorted_list_a, sorted_list_b):
        # return self.set_intersect_list(sorted_list_a, sorted_list_b)
        # return self.classic_double_looper(sorted_list_a, sorted_list_b)
        return self.simultaneous_walk_through_both_lists(sorted_list_a, sorted_list_b)

    # creating each set takes O(list size) time.
    def set_intersect_list(self, sorted_list_a, sorted_list_b):
        return list(set(sorted_list_a) & set(sorted_list_b))

    # classic O(longer list length ** 2)
    def classic_double_looper(self, sorted_list_a, sorted_list_b):
        intersection_list = []
        for elem_a in sorted_list_a:
            if elem_a in sorted_list_b and elem_a not in intersection_list:
                intersection_list.append(elem_a)
        return intersection_list

    # is list_a has n elem and list_b has m elem than at worst this is O(n+m) runtime and O(1) space
    def simultaneous_walk_through_both_lists(self, sorted_list_a, sorted_list_b):
        list_a_idx = 0
        list_b_idx = 0
        intersection_list = []
        while list_a_idx < len(sorted_list_a) and list_b_idx < len(sorted_list_b):
            if sorted_list_a[list_a_idx] < sorted_list_b[list_b_idx]:
                list_a_idx += 1
            elif sorted_list_a[list_a_idx] == sorted_list_b[list_b_idx]:
                # this if only works because of early terminating if statements!
                if not intersection_list or sorted_list_a[list_a_idx] != intersection_list[-1]:
                    intersection_list.append(sorted_list_a[list_a_idx])
                list_a_idx += 1
                list_b_idx += 1
            else:
                list_b_idx += 1
        return intersection_list
