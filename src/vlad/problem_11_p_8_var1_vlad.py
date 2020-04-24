from protocol.problem_11_p_8_var1 import Problem11P8Var1
import random
import heapq
import operator

"""
THINGS TO NOTE ABOUT THIS PROBLEM

"""


class Problem11P8Var1Vlad(Problem11P8Var1):
    def find_median(self, non_sorted_list):
        return self.modified_book_soln(non_sorted_list)

    def modified_book_soln(self, non_sorted_list):
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
            middle = (end - start + 1) // 2
            is_even = (end - start) % 2
            while True:
                pivot_idx = random.randint(start, end)
                pivot_idx = partition_list(start, end, pivot_idx)
                if pivot_idx == middle:
                    if is_even:
                        return (non_sorted_list[pivot_idx - 1] + non_sorted_list[pivot_idx]) / 2
                    return non_sorted_list[pivot_idx]
                elif pivot_idx < middle:
                    start = pivot_idx + 1
                else:
                    end = pivot_idx - 1
        return find_kth(operator.gt)
