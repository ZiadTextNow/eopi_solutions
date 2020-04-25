from protocol.problem_5_p_6 import Problem5P6
import sys

class Problem5P6Ziad(Problem5P6):
    def buy_and_sell_stock_once(self, prices):
        # return self.naive(prices)
        return self.better_solution(prices)

    # For each stock price, iterate through the remaining prices,
    # calculating the profit (or loss) each time and comparing it with the largest
    # profit seen so far, if greater, then update it.
    # time: O(n^2)
    # space: O(1)
    def naive(self, prices):
        largest_profit_so_far = 0

        for i in range(len(prices)):
            for j in range(i + 1, len(prices) - 1):
                current_profit = prices[j] - prices[i]
                largest_profit_so_far = max(largest_profit_so_far, current_profit)

        return largest_profit_so_far

    # Reduce problem to a single pass
    # time: O(n)
    # space: O(1)
    def better_solution(self, prices):
        max_profit_so_far, min_stock_price_so_far = 0, float('inf')

        for i in range(len(prices)):
            if prices[i] < min_stock_price_so_far:
                min_stock_price_so_far = prices[i]
            # find the profit that you would get if you would sell on the current day
            else:
                max_profit_so_far = max(max_profit_so_far, prices[i] - min_stock_price_so_far)

        return max_profit_so_far




prices = [310, 315, 275, 295, 260, 270, 290, 230, 255, 250]
print(Problem5P6Ziad().buy_and_sell_stock_once(prices))
