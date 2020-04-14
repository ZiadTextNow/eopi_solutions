import pytest
from vlad.problem_5_p_1_var4_vlad import Problem5P1Var4Vlad


class TestProblem5P1Var4(object):
    def instantiate_solution(self):
        return Problem5P1Var4Vlad()

    # True values were assigned integer values equal to list indices from 1 (couldn't start from 0 since 0 == False)
    # to make keeping track of order for True values easy when testing
    @pytest.mark.parametrize("unpartitioned_list, partitioned_list", [
        ([1, False, 3, False], [False, False, 1, 3]),
        (list(range(1, 4)) + [False] * 2, [False] * 2 + list(range(1, 4))),
        (list(range(1, 4)), list(range(1, 4))),
        ([False] * 3, [False] * 3),
    ])
    def test_bool_val_keep_true_order_partition(self, unpartitioned_list, partitioned_list):
        self.instantiate_solution().bool_val_keep_true_order_partition(unpartitioned_list)
        assert unpartitioned_list == partitioned_list


