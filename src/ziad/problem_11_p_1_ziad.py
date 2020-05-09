from protocol.problem_11_p_1 import Problem11P1

class Problem11P1Ziad(Problem11P1):
    def first_occurrence_of_k(self, sorted_list, k):
        return self.search_first_of_k(sorted_list, k)

        # iterative approach using binary search
        # time: O(log n)
        # space: O(1)
    def search_first_of_k(self, arr, k):
        lower, upper = 0, len(arr) - 1
        first_occurrence_of_k = -1

        if arr is None:
            return first_occurrence_of_k

        while lower <= upper:
            # avoid overflow
            midpoint = lower + (upper - lower) // 2

            if k < arr[midpoint]:
                upper = midpoint - 1
            elif k > arr[midpoint]:
                lower = midpoint + 1
            else:
                # k == midpoint, so record occurrence and try again to handle any previous occurrences
                first_occurrence_of_k = midpoint
                upper = midpoint - 1

        return first_occurrence_of_k
