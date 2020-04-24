import pytest
from vlad.problem_11_p_8_var1_vlad import Problem11P8Var1Vlad


class TestProblem11P8Var1(object):
    def instantiate_solution(self):
        return Problem11P8Var1Vlad()

    @pytest.mark.parametrize("non_sorted_list, median", [
        ([3, 2, 1, 5, 4], 3),
        ([3, 2, 1, 3, 5, 4], 3),
        (list(range(10)), 4.5),
    ])
    def test_find_median(self, non_sorted_list, median):
        assert self.instantiate_solution().find_median(non_sorted_list) == median
