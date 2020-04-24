from protocol.problem_11_p_8_var2 import Problem11P8Var2
import random
import operator

"""
THINGS TO NOTE ABOUT THIS PROBLEM

Not sure why book soln wouldn't work? Mine doesn't work cuz I use greater than or equal too compare but theirs is fine
cuz they use just greater than. If you use equal to you get stuck in infinite loop

"""


class Problem11P8Var2Vlad(Problem11P8Var2):
    def kth_largest_element_with_dups(self, non_sorted_list, k):
        # return self.divide_and_conquer_dis_shit(non_sorted_list, k)
        return self.book_soln(non_sorted_list, k)

    def divide_and_conquer_dis_shit(self, non_sorted_list, k):
        def inner_func(k, start, end):
            pivot_idx = random.randint(start, end)
            pivot_val = non_sorted_list[pivot_idx]
            start_ptr, end_ptr = start, end
            while start_ptr <= end_ptr:
                if non_sorted_list[start_ptr] < pivot_val:
                    start_ptr += 1
                elif non_sorted_list[end_ptr] >= pivot_val:
                    end_ptr -= 1
                else:
                    non_sorted_list[start_ptr], non_sorted_list[end_ptr] = non_sorted_list[end_ptr], non_sorted_list[start_ptr]
            elements_ge_to_pivot = end - end_ptr  # end_ptr is always the largest index with a val < pivot_val
            if elements_ge_to_pivot == k:
                return pivot_val
            elif elements_ge_to_pivot < k:  # if this is true we just remove all these elements
                end = end_ptr
                k -= elements_ge_to_pivot
                return inner_func(k, start, end)
            start = start_ptr
            return inner_func(k, start, end)
        return inner_func(k, 0, len(non_sorted_list) - 1)

    def book_soln(self, non_sorted_list, k):
        def find_kth(comp):
            def partition_list(start, end, pivot_idx):
                pivot_val = non_sorted_list[pivot_idx]
                non_sorted_list[pivot_idx], non_sorted_list[end] = non_sorted_list[end], non_sorted_list[pivot_idx]
                pivot_idx = start
                for i in range(start, end):
                    if comp(non_sorted_list[i], pivot_val):
                        non_sorted_list[i], non_sorted_list[pivot_idx] = non_sorted_list[pivot_idx], non_sorted_list[i]
                        pivot_idx += 1
                non_sorted_list[pivot_idx], non_sorted_list[end] = non_sorted_list[end], non_sorted_list[pivot_idx]
                return pivot_idx

            start, end = 0, len(non_sorted_list) - 1
            while True:
                pivot_idx = random.randint(start, end)
                pivot_idx = partition_list(start, end, pivot_idx)
                if pivot_idx == k - 1:
                    return non_sorted_list[pivot_idx]
                elif pivot_idx < k - 1:
                    start = pivot_idx + 1
                else:
                    end = pivot_idx - 1
        return find_kth(operator.gt)
