import pytest
from vlad.problem_15_p_1_var1_vlad import Problem15P1Var1Vlad


class TestProblem15P1Var1(object):
    def instantiate_solution(self):
        return Problem15P1Var1Vlad()

    """
    the operation are a list of tuples where each tuple has two values. The 
    first value is which peg we move the ring from. The second value is which 
    peg we move the ring to. The rings are assumed to start on Peg 0 and must be
    transferred to Peg 1
    """

    @pytest.mark.parametrize("n_rings, operations", [
        (1, [(0, 1)]),
        (2, [(0, 2), (0, 1), (2, 1)]),
        (3, [(0, 1), (0, 2), (1, 2), (0, 1), (2, 0), (2, 1), (0, 1)]),
        (4, [(0, 2), (0, 1), (2, 1), (0, 2), (1, 0), (1, 2), (0, 2), (0, 1),
             (2, 1), (2, 0), (1, 0), (2, 1), (0, 2), (0, 1), (2, 1)]),
    ])
    def test_towers_of_hanoi(self, n_rings, operations):
        assert self.instantiate_solution().towers_of_hanoi(
            n_rings) == operations
