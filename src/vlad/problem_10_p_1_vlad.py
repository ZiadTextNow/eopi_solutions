from protocol.problem_10_p_1 import Problem10P1
import heapq

"""
THINGS TO NOTE ABOUT THIS PROBLEM

"""


class Problem10P1Vlad(Problem10P1):
    def merge_sorted_lists(self, stock_price_lists):
        # return self.use_min_heap(stock_price_lists)
        return self.pythonic_soln(stock_price_lists)

    def use_min_heap(self, stock_price_lists):
        min_heap = [(stock_price_list[0], list_num, 1) for list_num, stock_price_list in enumerate(stock_price_lists)]
        heapq.heapify(min_heap)
        result_list = []
        while min_heap:
            lowest_stock_price, list_num, list_idx = heapq.heappop(min_heap)
            result_list.append(lowest_stock_price)
            if list_idx < len(stock_price_lists[list_num]):
                heapq.heappush(min_heap, (stock_price_lists[list_num][list_idx], list_num, list_idx + 1))

        return result_list

    # hacks!!!
    def pythonic_soln(self, stock_price_lists):
        return list(heapq.merge(*stock_price_lists))


