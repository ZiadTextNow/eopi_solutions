from protocol.problem_4_p_7 import Problem4P7


class Problem4P7Arshan(Problem4P7):
    def x_to_the_y(self, x, y):
        return self._faster_divide_and_conquer(x, y)
        return self._brute_force(x, y)
        return self._lazy_solution(x, y)


    """
    probably not faster
    """
    def _faster_divide_and_conquer(self, x, y):
        print(x, y)
        if y == 0:
            return 1
        if y == 1:
            return x
        left = self._faster_divide_and_conquer(x, y >> 1)
        right = self._faster_divide_and_conquer(x, y - (y >> 1))
        return left * right

    def _brute_force(self, x, y):
        num = 1
        for i in range(y):
            num *= x
        return num

    def _lazy_solution(self, x, y):
        return x ** y
