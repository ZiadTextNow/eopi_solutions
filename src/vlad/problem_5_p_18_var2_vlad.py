from protocol.problem_5_p_18_var2 import Problem5P18Var2
import math

"""
THINGS TO NOTE ABOUT THIS PROBLEM

"""


class Problem5P18Var2Vlad(Problem5P18Var2):
    def make_spiral_ordered_matrix_from_ints(self, int_list):
        return self.modified_single_step_book_soln(int_list)

    # same idea as from 5.18 except now you do it in the reverse order to build the matrix and use int_list as the vals
    def modified_single_step_book_soln(self, int_list):
        shift = ((0, 1), (1, 0), (0, -1), (-1, 0))
        dimension = int(math.sqrt(len(int_list)))   # this will always be an int since we are told list is size n**2
        spiral_ordered_matrix = [[0 for _ in range(dimension)] for _ in range(dimension)]
        x = y = 0
        direction = 0
        for val in int_list:
            spiral_ordered_matrix[x][y] = val
            next_x, next_y = x + shift[direction][0], y + shift[direction][1]
            if next_x == dimension or next_y == dimension or spiral_ordered_matrix[next_x][next_y]:
                direction = (direction + 1) & 3
                next_x, next_y = x + shift[direction][0], y + shift[direction][1]
            x, y = next_x, next_y
        return spiral_ordered_matrix


