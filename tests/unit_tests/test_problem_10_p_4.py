import pytest
from vlad.problem_10_p_4_vlad import Problem10P4Vlad


class TestProblem10P4(object):
    def instantiate_solution(self):
        return Problem10P4Vlad()

    @pytest.mark.parametrize("stars, k, k_closest_stars", [
        ([[1, 1, 1], [2, 2, 2], [3, 3, 3]], 1, [[1, 1, 1]]),
        ([[1, 1, 1], [2, 2, 2], [3, 3, 3]], 2, [[1, 1, 1], [2, 2, 2]]),
        ([[1, 1, 1], [2, 2, 2], [3, 3, 3]], 3, [[1, 1, 1], [2, 2, 2], [3, 3, 3]]),
    ])
    def test_k_closest_stars(self, stars, k, k_closest_stars):
        assert self.instantiate_solution().k_closest_stars(stars, k) == k_closest_stars

