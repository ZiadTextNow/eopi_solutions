import pytest

from arshan.problem_10_p_1_arshan import Problem10P1Arshan
from vlad.problem_10_p_1_vlad import Problem10P1Vlad
from ziad.problem_10_p_1_ziad import Problem10P1Ziad


class TestProblem10P1(object):
    def instantiate_solution(self):
        return Problem10P1Arshan()
        return Problem10P1Vlad()

    @pytest.mark.parametrize("stock_price_lists, result_list", [
        ([[3, 5, 7], [0, 6], [0, 6, 28]], [0, 0, 3, 5, 6, 6, 7, 28]),
        ([[1, 2, 3]], [1, 2, 3]),
        ([[1], [2], [3]], [1, 2, 3]),
        ([[1, 2], [3, 4], [5, 6]], [1, 2, 3, 4, 5, 6]),
    ])
    def test_merge_sorted_lists(self, stock_price_lists, result_list):
        assert self.instantiate_solution().merge_sorted_lists(stock_price_lists) == result_list
