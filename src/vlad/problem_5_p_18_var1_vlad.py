from protocol.problem_5_p_18_var1 import Problem5P18Var1

"""
THINGS TO NOTE ABOUT THIS PROBLEM

"""


class Problem5P18Var1Vlad(Problem5P18Var1):
    def make_spiral_ordered_matrix(self, dimension):
        return self.modified_single_step_book_soln(dimension)

    # same idea as from 5.18 except now you do it in the reverse order to build the matrix
    def modified_single_step_book_soln(self, dimension):
        shift = ((0, 1), (1, 0), (0, -1), (-1, 0))
        spiral_ordered_matrix = [[0 for _ in range(dimension)] for _ in range(dimension)]
        x = y = 0
        direction = 0
        for i in range(1, dimension**2 + 1):
            spiral_ordered_matrix[x][y] = i
            next_x, next_y = x + shift[direction][0], y + shift[direction][1]
            if next_x == dimension or next_y == dimension or spiral_ordered_matrix[next_x][next_y]:
                direction = (direction + 1) & 3
                next_x, next_y = x + shift[direction][0], y + shift[direction][1]
            x, y = next_x, next_y
        return spiral_ordered_matrix


