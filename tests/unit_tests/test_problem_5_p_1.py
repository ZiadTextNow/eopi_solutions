import pytest
# from vlad.problem_5_p_1_vlad import Problem5P1Vlad
from ziad.problem_4_p_1_ziad import Problem4P1Ziad


class TestProblem5P1(object):
    def instantiate_solution(self):
        # return Problem5P1Vlad()
        return Problem4P1Ziad

    """
    equal_idx is leftmost idx where value == pivot
    high_idx is leftmost idx where value > pivot. If no values in list exist that are > pivot then high_idx is None 
    """
    @pytest.mark.parametrize("pivot_index, unpartitioned_list, equal_idx, high_idx", [
        (3, [-3, 0, -1, 1, 1, -5, 1, 3, 4, 2], 4, 7),
        (0, [0], 0, None),
        (2, [9, 8, 7, 6, 5, 4, 3, 2, 1, 0], 7, 8)
    ])
    def test_dutch_flag_partition(self, pivot_index, unpartitioned_list, equal_idx, high_idx):
        pivot = unpartitioned_list[pivot_index]
        self.instantiate_solution().dutch_flag_partition(pivot_index, unpartitioned_list)
        # TODO: I feel like these asserts are super messy but wasn't sure how to make it cleaner :(
        # if equal_idx == 0 then there are no values < pivot and this assert returns True
        assert max(unpartitioned_list[:equal_idx]) < pivot if equal_idx else True
        assert max(unpartitioned_list[equal_idx:high_idx]) == min(unpartitioned_list[equal_idx:high_idx]) == pivot
        # if high_idx == None then there are no values > pivot and this assert returns True
        assert min(unpartitioned_list[high_idx:]) > pivot if high_idx else True

