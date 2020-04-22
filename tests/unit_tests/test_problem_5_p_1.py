import pytest

from arshan.problem_5_p_1_arshan import Problem5P1Arshan
from vlad.problem_5_p_1_vlad import Problem5P1Vlad


class TestProblem5P1(object):
    def instantiate_solution(self):
        return Problem5P1Arshan()
        #return Problem5P1Vlad()

    @pytest.mark.parametrize("pivot_index, unpartitioned_list", [
        (3, [-3, 0, -1, 1, 1, -5, 1, 3, 4, 2]),
        (0, [0]),
        (2, [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]),
        (5, [10, 9, 8, 7, 6, 5])
    ])
    def test_dutch_flag_partition(self, pivot_index, unpartitioned_list):
        pivot_value = unpartitioned_list[pivot_index]
        first_index_beq_pivot = len(unpartitioned_list)
        partitioned_list = self.instantiate_solution().dutch_flag_partition(pivot_index, unpartitioned_list)
        assert len(partitioned_list) == len(unpartitioned_list)
        for i, value in enumerate(partitioned_list):
            if value >= pivot_value:
                first_index_beq_pivot = i
                break
        first_index_b_pivot = len(unpartitioned_list)
        for i in range(first_index_beq_pivot, len(partitioned_list)):
            value = partitioned_list[i]
            if value > pivot_value:
                first_index_b_pivot = i
                break
        for i in range(first_index_beq_pivot):
            assert partitioned_list[i] < pivot_value
        for i in range(first_index_beq_pivot, first_index_b_pivot):
            assert partitioned_list[i] == pivot_value
        for i in range(first_index_b_pivot, len(partitioned_list)):
            assert partitioned_list[i] > pivot_value

