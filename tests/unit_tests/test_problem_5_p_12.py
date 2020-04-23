import random

from matplotlib import pyplot
import pytest

from arshan.problem_5_p_12_arshan import Problem5P12Arshan
from vlad.problem_5_p_12_vlad import Problem5P12Vlad


class TestProblem5P12(object):
    def instantiate_solution(self):
        #return Problem5P12Arshan()
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


    """
    In this test I fix the size to 1 (selecting 1 value only) then I'll 
    run the function on the input of range(100) a number of times, then 
    I will draw a histogram of all the selected indices...
    I also do the same using the random.randint function, and compare 
    the two histograms visually to see how similar they are.
    """
    def test_histogram(self):
        input_list = list(range(100))
        num_experiments = 1000000
        solution_outputs = []
        perfect_outputs = []
        solution = self.instantiate_solution()
        for _ in range(num_experiments):
            solution_outputs.append(
                solution.random_sampling(input_list.copy(), 1)[0]
            )
            perfect_outputs.append(random.randint(0, 99))
        _ = pyplot.hist(solution_outputs, bins=100)
        _ = pyplot.hist(perfect_outputs, bins=100)
        pyplot.show()
