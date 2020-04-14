import pytest
from vlad.problem_5_p_1_vlad import Problem5P1Vlad


class TestProblem5P1(object):
    def instantiate_solution(self):
        return Problem5P1Vlad()

    """
    equal_idx is leftmost idx where value == pivot
    high_idx is leftmost idx where value > pivot. If no values in list exist that are > pivot then high_idx is None 
    """
    @pytest.mark.parametrize("pivot_index, unsorted_list, equal_idx, high_idx", [
        (3, [-3, 0, -1, 1, 1, -5, 1, 3, 4, 2], 4, 7),
        (0, [0], 0, None),
        (2, [9, 8, 7, 6, 5, 4, 3, 2, 1, 0], 7, 8)
    ])
    def test_dutch_flag_partition(self, pivot_index, unsorted_list, equal_idx, high_idx):
        pivot = unsorted_list[pivot_index]
        self.instantiate_solution().dutch_flag_partition(pivot_index, unsorted_list)
        # TODO: I feel like these asserts are super messy but wasn't sure how to make it cleaner :(
        # if equal_idx == 0 then there are no values < pivot and this assert returns True
        assert max(unsorted_list[:equal_idx]) < pivot if equal_idx else True
        assert max(unsorted_list[equal_idx:high_idx]) == min(unsorted_list[equal_idx:high_idx]) == pivot
        # if high_idx == None then there are no values > pivot and this assert returns True
        assert min(unsorted_list[high_idx:]) > pivot if high_idx else True

