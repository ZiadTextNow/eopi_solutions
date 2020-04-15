import pytest
from vlad.problem_5_p_12_vlad import Problem5P12Vlad


class TestProblem5P12(object):
    def instantiate_solution(self):
        return Problem5P12Vlad()

    """
    Testing for randomness is very hard and from my research I couldn't find a reasonably quick way to test for it so
    for now I just make sure the returned list and visually inspect the result by printing it and running multiple times
    """
    @pytest.mark.parametrize("distinct_elem_list, size", [
        ([1, 2, 3, 4], 0),
        ([1, 2, 3, 4], 1),
        ([1, 2, 3, 4], 2),
        ([1, 2, 3, 4], 3),
        ([1, 2, 3, 4], 4),
        ([310, 315, 275, 295, 260, 270, 290, 230, 255, 250], 3),
        ([1], 1),
    ])
    def test_random_sampling(self, distinct_elem_list, size):
        original_list_len = len(distinct_elem_list)
        self.instantiate_solution().random_sampling(distinct_elem_list, size)
        print(distinct_elem_list)
        assert original_list_len == len(distinct_elem_list)
