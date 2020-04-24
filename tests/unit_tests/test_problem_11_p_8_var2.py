import pytest
from vlad.problem_11_p_8_var2_vlad import Problem11P8Var2Vlad


class TestProblem11P8Var2(object):
    def instantiate_solution(self):
        return Problem11P8Var2Vlad()

    @pytest.mark.parametrize("non_sorted_list, k, kth_largest_element", [
        ([3, 2, 1, 5, 4], 1, 5),
        ([3, 2, 1, 5, 4], 3, 3),
        ([3, 2, 1, 5, 4], 5, 1),
        ([3, 2, 1, 1, 2, 5, 5, 4], 2, 5),
        ([3, 2, 1, 1, 2, 5, 5, 4], 8, 1),
        ([3, 2, 1, 1, 2, 5, 5, 4], 5, 2),
        (list(range(10)), 1, 9),
        (list(range(10)), 10, 0),
        (list(range(10)), 5, 5),
        ([1, 2, 3, 1, 2, 3, 3, 2, 1], 5, 2),
        ([1, 2, 3, 1, 2, 3, 3, 2, 1], 1, 3),
        ([1, 2, 3, 1, 2, 3, 3, 2, 1], 2, 3),
        ([1, 2, 3, 1, 2, 3, 3, 2, 1], 3, 3),
    ])
    def test_kth_largest_element_with_dups(self, non_sorted_list, k, kth_largest_element):
        assert self.instantiate_solution().kth_largest_element_with_dups(non_sorted_list, k) == kth_largest_element
