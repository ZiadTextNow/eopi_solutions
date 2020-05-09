from protocol.problem_11_p_4 import Problem11P4

"""
THINGS TO NOTE ABOUT THIS PROBLEM

"""


class Problem11P4Vlad(Problem11P4):
    def integer_square_root(self, non_neg_int):
        # return self.iterative_modified_bsearch(non_neg_int)
        return self.recursive_modified_bsearch(non_neg_int)

    def iterative_modified_bsearch(self, non_neg_int):
        start, end = 0, non_neg_int
        while end >= start:
            half = start + (end - start) // 2
            half_sqr = half ** 2
            if half_sqr == non_neg_int:
                return half
            elif half_sqr > non_neg_int:
                end = half - 1
            else:
                start = half + 1
                best_result_so_far = half
        return best_result_so_far

    def book_soln(self, non_neg_int):
        start, end = 0, non_neg_int
        while end >= start:
            half = start + (end - start) // 2
            half_sqr = half ** 2
            if half_sqr <= non_neg_int:
                start = half + 1
            elif half_sqr > non_neg_int:
                end = half - 1
        return start - 1   # this is smart since start is always going to 1 more than the correct value

    def recursive_modified_bsearch(self, non_neg_int):
        def inner_func(start, end):
            if end < start:
                return None
            half = start + (end - start) // 2
            half_sqr = half ** 2
            if half_sqr == non_neg_int:
                return half
            elif half_sqr > non_neg_int:
                return inner_func(start, half - 1)
            else:
                larger_half = inner_func(half + 1, end)
                if larger_half:
                    return larger_half
                return half

        return inner_func(0, non_neg_int)
