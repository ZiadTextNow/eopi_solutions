import pytest
from vlad.problem_5_p_6_vlad import Problem5P6Vlad


class TestProblem5P6(object):
    def instantiate_solution(self):
        return Problem5P6Vlad()

    @pytest.mark.parametrize("prices, max_profit", [
        ([1, 2, 3], 2),
        ([310, 315, 275, 295, 260, 270, 290, 230, 255, 250], 30),
        ([9, 8, 2, 1], 0)
    ])
    def test_buy_and_sell_stock_once(self, prices, max_profit):
        assert self.instantiate_solution().buy_and_sell_stock_once(prices) == max_profit
