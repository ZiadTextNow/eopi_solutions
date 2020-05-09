import pytest

from arshan.problem_11_p_1_arshan import Problem11P1Arshan
from vlad.problem_11_p_1_vlad import Problem11P1Vlad
from ziad.problem_11_p_1_ziad import Problem11P1Ziad


class TestProblem11P1(object):
    def instantiate_solution(self):
        return Problem11P1Arshan()
        return Problem11P1Vlad()
        # return Problem11P1Ziad()

    @pytest.mark.parametrize("sorted_list, k, k_idx", [
        ([1, 2, 3, 4, 5], 3, 2),
        ([1, 2, 3, 3, 3, 4, 5], 3, 2),
        ([1, 1, 1], 1, 0),
    ])
    def test_first_occurrence_of_k(self, sorted_list, k, k_idx):
        assert self.instantiate_solution().first_occurrence_of_k(sorted_list, k) == k_idx
