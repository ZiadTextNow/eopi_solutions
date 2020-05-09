from protocol.problem_10_p_1 import Problem10P1
import heapq


class Problem10P1Ziad(Problem10P1):
    def merge_sorted_lists(self, stock_price_lists):
        return self.merge_sorted_lists(stock_price_lists)

    def merge_sorted_lists(self, lists):
        array_iterators = [iter(x) for x in lists]
        min_heap = []
        merged_list = []

        for i, iterator in enumerate(array_iterators):
            first = next(iterator, None)
            if first: heapq.heappush(min_heap, (first, i))

        while min_heap:
            min_val, smallest_array_index = heapq.heappop(min_heap)
            smallest_iterator = array_iterators[smallest_array_index]

            merged_list.append(min_val)

            next_val = next(smallest_iterator, None)
            if next_val:
                heapq.heappush(min_heap, (next_val, smallest_array_index))

        return merged_list




