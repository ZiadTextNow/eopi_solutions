import pytest
from vlad.problem_11_p_8_vlad import Problem11P8Vlad


class TestProblem11P8(object):
    def instantiate_solution(self):
        return Problem11P8Vlad()

    @pytest.mark.parametrize("non_sorted_list, k, kth_largest_element", [
        ([3, 2, 1, 5, 4], 1, 5),
        ([3, 2, 1, 5, 4], 3, 3),
        ([3, 2, 1, 5, 4], 5, 1),
        (list(range(10)), 1, 9),
        (list(range(10)), 10, 0),
        (list(range(10)), 5, 5),
    ])
    def test_kth_largest_element(self, non_sorted_list, k, kth_largest_element):
        assert self.instantiate_solution().kth_largest_element(non_sorted_list, k) == kth_largest_element
