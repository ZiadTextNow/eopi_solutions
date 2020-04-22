from protocol.problem_11_p_1 import Problem11P1

"""
THINGS TO NOTE ABOUT THIS PROBLEM

This is exactly the same problem as the having infinitely many identical eggs that all break starting at floor x and
onward and you have to fly floor x since all floors before floor x can be considered as 0 and all floors x and up can 
be 1. Then you have to find the first occurrence of 1 which would k in the general case of this problem!
Had the egg problem for google interview FYI
"""


class Problem11P1Vlad(Problem11P1):
    def first_occurrence_of_k(self, sorted_list, k):
        # return self.iterative_modified_bsearch(sorted_list, k)
        return self.recursive_modified_bsearch(sorted_list, k)

    def iterative_modified_bsearch(self, sorted_list, k):
        start, end = 0, len(sorted_list) - 1
        k_idx = None
        while end >= start:
            half_way_idx = start + (end - start) // 2   # this is the last idx of the smaller valued list
            half_way_val = sorted_list[half_way_idx]
            if k == half_way_val:
                k_idx = half_way_idx
                end = half_way_idx - 1
            elif k < half_way_val:
                end = half_way_idx - 1
            else:
                start = half_way_idx + 1
        return k_idx

    def recursive_modified_bsearch(self, sorted_list, k):
        def inner_func(k, start, end):
            if end < start:
                return None
            half_way_idx = start + (end - start) // 2  # this is the last idx of the smaller valued list
            half_way_val = sorted_list[half_way_idx]
            if k == half_way_val:
                idx_in_lower_half = inner_func(k, start, half_way_idx - 1)
                if idx_in_lower_half is not None:  # better to be verbose and say not None cuz now int val of 0 is True
                    return idx_in_lower_half
                return half_way_idx
            elif k < half_way_val:
                return inner_func(k, start, half_way_idx - 1)
            else:
                return inner_func(k, half_way_idx + 1, end)
        return inner_func(k, 0, len(sorted_list) - 1)
