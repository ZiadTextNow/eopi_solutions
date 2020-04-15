import pytest
from vlad.problem_5_p_18_var6_vlad import Problem5P18Var6Vlad


class TestProblem5P18Var6(object):
    def instantiate_solution(self):
        return Problem5P18Var6Vlad()

    @pytest.mark.parametrize("non_sqr_matrix, k, kth_elem", [
        # ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 5, 8),
        # ([[1, 2, 3], [7, 8, 9]], 2, 3),
        # ([[1, 2, 3]], 1, 2),
        ([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]], 10, 9),
        ([[1, 2, 3, 4], [5, 6, 7, 8], [13, 14, 15, 16]], 7, 13),
        ([[1, 2, 3, 4], [5, 6, 7, 8]], 5, 7),
        ([[1, 2, 3], [5, 6, 7]], 5, 5),
        ([[1, 3], [5, 7]], 0, 1),
        ([[1], [7]], 1, 7),
        ([[7]], 0, 7),
        ([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]], 13, 16),
    ])
    def test_kth_elem_spiral_order(self, non_sqr_matrix, k, kth_elem):
        assert self.instantiate_solution().kth_elem_spiral_order(non_sqr_matrix, k) == kth_elem
