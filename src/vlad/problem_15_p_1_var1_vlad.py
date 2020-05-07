from protocol.problem_15_p_1_var1 import Problem15P1Var1

"""
THINGS TO NOTE ABOUT THIS PROBLEM

"""


class Problem15P1Var1Vlad(Problem15P1Var1):
    def towers_of_hanoi(self, n_rings):
        # return self.iterative_shit(n_rings)
        return self.another_iterative_one(n_rings)

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
    def iterative_shit(self, n_rings):
        operations = []
        call_stack = []
        cur_peg = 0
        goal_peg = 1
        temp_peg = 2
        n_rings -= 1
        call_stack.append((n_rings, cur_peg, goal_peg, temp_peg))
        while call_stack:
            if n_rings == 0:
                n_rings, cur_peg, goal_peg, temp_peg = call_stack.pop()
                operations.append((cur_peg, goal_peg))
                cur_peg, goal_peg, temp_peg = temp_peg, goal_peg, cur_peg
                goal_peg, temp_peg = temp_peg, goal_peg
            if n_rings > 0:
                n_rings -= 1
                goal_peg, temp_peg = temp_peg, goal_peg
                call_stack.append((n_rings, cur_peg, goal_peg, temp_peg))

        return operations

    """
    I like this one much more! It's way more clean and easy to understand.
    The idea behind it is to replace recursive call stack with a stack
    you n_rings to represent how many rings you have above the current ring you
    want to move. Otherwise it actually identical to the iterative solution for
    and in-order tree traversal
    """
    def another_iterative_one(self, n_rings):
        operations = []
        call_stack = []
        cur_peg = 0
        goal_peg = 1
        temp_peg = 2
        while True:
            if n_rings > 0:
                n_rings -= 1
                call_stack.append((n_rings, cur_peg, goal_peg, temp_peg))
                goal_peg, temp_peg = temp_peg, goal_peg
            elif call_stack:
                n_rings, cur_peg, goal_peg, temp_peg = call_stack.pop()
                operations.append((cur_peg, goal_peg))
                cur_peg, temp_peg = temp_peg, cur_peg
            else:
                break

        return operations
