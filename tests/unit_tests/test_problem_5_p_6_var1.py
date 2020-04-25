import pytest
from vlad.problem_5_p_6_var1_vlad import Problem5P6Var1Vlad
# from ziad.problem_4_p_1_var1_ziad import Problem5P6Var1Ziad

class TestProblem5P6Var1(object):
    def instantiate_solution(self):
        return Problem5P6Var1Vlad()
        # return Problem5P6Var1Ziad()

    @pytest.mark.parametrize("int_list, longest_sublist", [
        ([1, 2, 2], 2),
        ([2, 2, 1], 2),
        ([310, 315, 275, 295, 260, 270, 290, 230, 255, 250], 1),
        ([9, 9, 9, 9], 4)
    ])
    def test_find_longest_equal_sublist(self, int_list, longest_sublist):
        assert self.instantiate_solution().find_longest_equal_sublist(int_list) == longest_sublist
