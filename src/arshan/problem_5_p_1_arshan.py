from protocol.problem_5_p_1 import Problem5P1


class Problem5P1Arshan(Problem5P1):
    def dutch_flag_partition(self, pivot_index, unpartitioned_list):
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














