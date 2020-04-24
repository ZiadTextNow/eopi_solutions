from protocol.problem_11_p_8 import Problem11P8
import random
import heapq
import operator

"""
THINGS TO NOTE ABOUT THIS PROBLEM

"""


class Problem11P8Vlad(Problem11P8):
    def kth_largest_element(self, non_sorted_list, k):
        # return self.sort_and_find(non_sorted_list, k)
        # return self.using_heap(non_sorted_list, k)
        # return self.divide_and_conquer_dis_shit(non_sorted_list, k)
        return self.book_soln(non_sorted_list, k)

    # runtime: O(nlogn), space: O(1)
    def sort_and_find(self, non_sorted_list, k):
        non_sorted_list.sort()
        return non_sorted_list[-k]

    # runtime: O(nlogk), space: O(k)
    def using_heap(self, non_sorted_list, k):
        min_heap = non_sorted_list[:k]
        heapq.heapify(min_heap)
        for i in range(k, len(non_sorted_list)):
            heapq.heappushpop(min_heap, non_sorted_list[i])
        return heapq.heappop(min_heap)

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
