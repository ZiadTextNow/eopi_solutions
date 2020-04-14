import pytest
from vlad.problem_5_p_1_var3_vlad import Problem5P1Var3Vlad


class TestProblem5P1Var3(object):
    def instantiate_solution(self):
        return Problem5P1Var3Vlad()

    @pytest.mark.parametrize("unpartitioned_list, partitioned_list", [
        ([True, False, True, False], [False, False, True, True]),
        ([True] * 3 + [False] * 2, [False] * 2 + [True] * 3),
        ([True] * 3, [True] * 3),
        ([False] * 3, [False] * 3),
    ])
    def test_four_val_partition(self, unpartitioned_list, partitioned_list):
        self.instantiate_solution().bool_val_partition(unpartitioned_list)
        assert unpartitioned_list == partitioned_list

