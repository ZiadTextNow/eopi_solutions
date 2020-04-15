import pytest
from vlad.problem_5_p_18_var2_vlad import Problem5P18Var2Vlad


class TestProblem5P18Var2(object):
    def instantiate_solution(self):
        return Problem5P18Var2Vlad()

    @pytest.mark.parametrize("int_list, spiral_ordered_matrix", [
        (list(range(1, 10)), [[1, 2, 3], [8, 9, 4], [7, 6, 5]]),
        (list(range(1, 17)), [[1, 2, 3, 4], [12, 13, 14, 5], [11, 16, 15, 6], [10, 9, 8, 7]]),
        (list(range(1, 26)),
         [[1, 2, 3, 4, 5], [16, 17, 18, 19, 6], [15, 24, 25, 20, 7], [14, 23, 22, 21, 8], [13, 12, 11, 10, 9]])
    ])
    def test_make_spiral_ordered_matrix_from_ints(self, int_list, spiral_ordered_matrix):
        assert self.instantiate_solution().make_spiral_ordered_matrix_from_ints(int_list) == spiral_ordered_matrix
