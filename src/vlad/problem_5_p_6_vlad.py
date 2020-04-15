from protocol.problem_5_p_6 import Problem5P6

"""
THINGS TO NOTE ABOUT THIS PROBLEM

"""


class Problem5P6Vlad(Problem5P6):
    def buy_and_sell_stock_once(self, prices):
        return self.one_pass(prices)

    def brute_force(self, prices):
        max_profit = 0
        for i in range(len(prices)):
            for j in range(i, len(prices)):
                if prices[j] - prices[i] > max_profit:
                    max_profit = prices[j] - prices[i]
        return max_profit

    def one_pass(self, prices):
        max_profit = 0
        min_price = float('inf')
        for price in prices:
            if price < min_price:
                min_price = price
            elif price - min_price > max_profit:
                max_profit = price - min_price
        return max_profit
