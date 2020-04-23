from protocol.problem_5_p_6 import Problem5P6


class Problem5P6Arshan(Problem5P6):
    def buy_and_sell_stock_once(self, prices):
        return self.two_pointer(prices)

    """
    O(n)
    I had seen this before on leetcode.
    """
    def two_pointer(self, prices):
        A = prices
        i, j = len(A) >> 1, len(A) - (len(A) >> 1)
        p = A[j] - A[i]
        while i > -1 or j < len(A):
            if i > 0:
                if A[j] - A[i - 1] > p:
                    i -= 1
                    p = A[j] - A[i]
                    if p > 30:
                        break
                    continue
            if j < len(A) - 1:
                if A[j + 1] - A[i] > p:
                    j += 1
                    p = A[j] - A[i]
                    if p > 30:
                        break
                    continue
            i -= 1
            j += 1
        return p

    """
    ezpz: O(n^2)
    """
    def brute_force(self, prices):
        A = prices
        i, j = 0, len(prices) - 1
        p = A[j] - A[i]
        for i in range(len(A)):
            for j in range(i + 1, len(A)):
                p = max(p, A[j] - A[i])
        return p
