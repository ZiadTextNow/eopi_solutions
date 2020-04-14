import pytest
from vlad.problem_5_p_1_var2_vlad import Problem5P1Var2Vlad


class TestProblem5P1Var1(object):
    def instantiate_solution(self):
        return Problem5P1Var2Vlad()

    @pytest.mark.parametrize("unpartitioned_list", [
        [1, 2, 3, 4, 1, 2, 3, 4],
        [4, 3, 2, 1, 4, 3, 2, 1],
        [1, 1, 2, 2, 3, 3, 4, 4],
        [1, 1000, 100, 10, 100, 1000, 10, 1, 1, 1, 10],
    ])
    def test_four_val_partition(self, unpartitioned_list):
        copy_unpartitioned_list = list(unpartitioned_list)   # keep a copy of original list for value comparison later
        self.instantiate_solution().four_val_partition(unpartitioned_list)
        # the list is partitioned in three groups if walking through the list only detects two value changes
        value_changes = 0
        prev_val = unpartitioned_list[0]
        all_vals_list = [prev_val]
        for val in unpartitioned_list:
            if val != prev_val:
                value_changes += 1
                all_vals_list.append(val)
            prev_val = val
        assert value_changes == 3
        assert len(copy_unpartitioned_list) == len(unpartitioned_list)
        # check that values in the partitioned list as actually the same values that appeared in the original list
        for val in all_vals_list:
            assert val in copy_unpartitioned_list



