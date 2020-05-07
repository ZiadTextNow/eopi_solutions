from protocol.problem_15_p_1 import Problem15P1

"""
THINGS TO NOTE ABOUT THIS PROBLEM

"""


class Problem15P1Vlad(Problem15P1):
    def towers_of_hanoi(self, n_rings):
        return self.recursive_shit(n_rings)

    """
    after writing the test case I analyzed what was happening. Below is the test
    case:
    (1, [(0, 1)]),
    (2, [(0, 2), 
         (0, 1), 
         (2, 1)]),
    (3, [(0, 1), (0, 2), (1, 2), 
         (0, 1), 
         (2, 0), (2, 1), (0, 1)]),
    (4, [(0, 2), (0, 1), (2, 1), (0, 2), (1, 0), (1, 2), (0, 2), 
         (0, 1),
         (2, 1), (2, 0), (1, 0), (2, 1), (0, 2), (0, 1), (2, 1)]),
    rewriting the way I did above you can see there is always the step in the 
    middle to the largest ring to middle peg then just do the steps before it
    but with Peg 0 swapped for Peg 2 or vice versa
    """
    def recursive_shit(self, n_rings):
        def inner_func(n_rings, goal_peg, temp_peg):
            if n_rings > 0:
                inner_func(n_rings - 1, temp_peg, goal_peg)

                cur_peg = 3 - goal_peg - temp_peg
                operations.append((cur_peg, goal_peg))

                inner_func(n_rings - 1, goal_peg, cur_peg)

        operations = []
        inner_func(n_rings, 1, 2)
        return operations
