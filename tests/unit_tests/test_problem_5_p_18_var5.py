import pytest
from vlad.problem_5_p_18_var5_vlad import Problem5P18Var5Vlad


class TestProblem5P18Var5(object):
    def instantiate_solution(self):
        return Problem5P18Var5Vlad()

    @pytest.mark.parametrize("non_sqr_matrix, last_elem", [
        # ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 5),
        ([[1, 2, 3], [7, 8, 9]], 7),
        ([[1, 2, 3]], 3),
        ([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]], 10),
        ([[1, 2, 3, 4], [5, 6, 7, 8], [13, 14, 15, 16]], 7),
        ([[1, 2, 3, 4], [5, 6, 7, 8]], 5),
        ([[1, 2, 3], [5, 6, 7]], 5),
        ([[1, 3], [5, 7]], 5),
        ([[1], [7]], 7),
        ([[7]], 7),
        ([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]], 13),
    ])
    def test_last_elem_spiral_order(self, non_sqr_matrix, last_elem):
        assert self.instantiate_solution().last_elem_spiral_order(non_sqr_matrix) == last_elem
