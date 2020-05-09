import pytest
from vlad.problem_15_p_2_vlad import Problem15P2Vlad


class TestProblem15P2(object):
    def instantiate_solution(self):
        return Problem15P2Vlad()

    """
    row and column indices start from 0. Results are to be in format of a 
    list of lists where each inner list contains a tuple of each queen position
    """
    @pytest.mark.parametrize("n, placements", [
        (1, [[(0, 0)]]),
        (2, []),
        (3, []),
        (4, [[(0, 1), (1, 3), (2, 0), (3, 2)],
             [(0, 2), (1, 0), (2, 3), (3, 1)]]),
    ])
    def test_non_attacking_placements_of_n_queens(self, n, placements):
        assert self.instantiate_solution().\
            non_attacking_placements_of_n_queens(n) == placements
