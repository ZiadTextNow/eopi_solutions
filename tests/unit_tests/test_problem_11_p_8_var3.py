import pytest
from vlad.problem_11_p_8_var3_vlad import Problem11P8Var3Vlad
from protocol.problem_11_p_8_var3 import Building


class TestProblem11P8Var3(object):
    def instantiate_solution(self):
        return Problem11P8Var3Vlad()

    """
    There can be multiple solutions to this problem assuming only integer solutions are 
    allowed. So any of the correct solutions are accepted
    """
    @pytest.mark.parametrize("building_tuples, mailbox_distance", [
        ([(2, 0), (3, 1), (1, 2)], [1]),
        ([(3, 1), (2, 0), (1, 2)], [1]),
        ([(1, 5), (1, 4), (1, 3), (1, 2), (1, 1), (1, 0)], [2, 3]),
        ([(1, 5), (1, 4), (0, 3), (1, 2), (1, 1), (1, 0)], [2]),
        ([(1, 5), (0, 4), (0, 3), (1, 2), (1, 1), (1, 0)], [1, 2]),
    ])
    def test_place_the_mailbox(self, building_tuples, mailbox_distance):
        buildings = []
        for i in range(len(building_tuples)):
            buildings.append(Building(building_tuples[i][0], building_tuples[i][1]))
        assert self.instantiate_solution().place_the_mailbox(buildings) in mailbox_distance
