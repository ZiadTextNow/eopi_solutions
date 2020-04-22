from protocol.problem_5_p_1 import Problem5P1


class Problem5P1Arshan(Problem5P1):
    def dutch_flag_partition(self, pivot_index, unpartitioned_list):
        return self._less_space(pivot_index, unpartitioned_list)
        return self._books_solution(pivot_index, unpartitioned_list)
        return self._lazy_solution(pivot_index, unpartitioned_list)

    def _books_solution(self, pivot_index, A):
        pivot = A[pivot_index]
        for i in range(len(A)):
            for j in range(i+1, len(A)):
                if A[j] < pivot:
                    A[i], A[j] = A[j], A[i]
                    break
        for i in reversed(range(len(A))):
            if A[i] < pivot:
                break
            for j in reversed(range(i)):
                if A[j] > pivot:
                    A[i], A[j] = A[j], A[i]
                    break
        return A
    """
    O(n^2): worst complexity
    idea: 
         - do a lil swappy swap if it's to the left of pivot
         - do a lil shifty shift if it's to the right of pivot
    best case:
        - more swaps will result in less complexity O(n)
        - more shifts will probably result in more complexity
    """
    def _less_space(self, pivot_index, unpartitioned_list):
        i = 0
        while i < len(unpartitioned_list):
            if i < pivot_index:
                if unpartitioned_list[i] > unpartitioned_list[pivot_index]:
                    unpartitioned_list[i], unpartitioned_list[pivot_index] = unpartitioned_list[pivot_index], unpartitioned_list[i]
                    pivot_index = i
            else:
                if unpartitioned_list[i] < unpartitioned_list[pivot_index]:
                    unpartitioned_list[pivot_index:i+1] = [unpartitioned_list[i]] + unpartitioned_list[pivot_index:i]
                    pivot_index += 1
            i += 1
        return unpartitioned_list

    """
    O(n)
    Go through the array 3 times:
    append all less
    append all equal
    append all bigger
    """
    def _lazy_solution(self, pivot_index, unpartitioned_list):
        partitioned = []
        pivot_value = unpartitioned_list[pivot_index]
        for i, value in enumerate(unpartitioned_list):
            if value < pivot_value:
                partitioned.append(value)
        for i, value in enumerate(unpartitioned_list):
            if value == pivot_value:
                partitioned.append(value)
        for i, value in enumerate(unpartitioned_list):
            if value > pivot_value:
                partitioned.append(value)
        return partitioned











