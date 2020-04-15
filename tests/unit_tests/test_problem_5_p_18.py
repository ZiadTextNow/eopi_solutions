import pytest
from vlad.problem_5_p_18_vlad import Problem5P18Vlad


class TestProblem5P18(object):
    def instantiate_solution(self):
        return Problem5P18Vlad()

    @pytest.mark.parametrize("two_d_list, spiral_ordered_list", [
        ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [1, 2, 3, 6, 9, 8, 7, 4, 5]),
        ([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]],
         [1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10]),
        ([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]],
         [1, 2, 3, 4, 5, 10, 15, 20, 25, 24, 23, 22, 21, 16, 11, 6, 7, 8, 9, 14, 19, 18, 17, 12, 13]),
    ])
    def test_spiral_ordering(self, two_d_list, spiral_ordered_list):
        assert self.instantiate_solution().spiral_ordering(two_d_list) == spiral_ordered_list
