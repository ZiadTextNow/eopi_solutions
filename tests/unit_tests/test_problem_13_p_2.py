import pytest
from vlad.problem_13_p_2_vlad import Problem13P2Vlad


class TestProblem13P2(object):
    def instantiate_solution(self):
        return Problem13P2Vlad()

    @pytest.mark.parametrize("sorted_list_a, sorted_list_b, merged_list", [
        ([5, 13, 17] + ['_'] * 5, [3, 7, 11, 19], [3, 5, 7, 11, 13, 17, 19, '_']),
    ])
    def test_merge_two_sorted_lists(self, sorted_list_a, sorted_list_b, merged_list):
        assert self.instantiate_solution().merge_two_sorted_lists(sorted_list_a, sorted_list_b) == merged_list
