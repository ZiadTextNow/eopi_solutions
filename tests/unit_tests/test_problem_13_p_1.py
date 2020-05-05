import pytest
from vlad.problem_13_p_1_vlad import Problem13P1Vlad


class TestProblem13P1(object):
    def instantiate_solution(self):
        return Problem13P1Vlad()

    @pytest.mark.parametrize("sorted_list_a, sorted_list_b, intersection_list", [
        ([2, 3, 3, 5, 5, 6, 7, 7, 8, 12], [5, 5, 6, 8, 8, 9, 10, 10], [5, 6, 8]),
        ([2, 3, 3, 5, 5, 6, 7, 7, 8, 12], [], []),
        ([], [5, 5, 6, 8, 8, 9, 10, 10], []),
    ])
    def test_intersection_of_two_sorted_lists(self, sorted_list_a, sorted_list_b, intersection_list):
        # we use set since book doesn't say order should matter
        assert set(self.instantiate_solution().intersection_of_two_sorted_lists(sorted_list_a, sorted_list_b)) == set(
            intersection_list)
