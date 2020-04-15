from protocol.problem_5_p_18_var4 import Problem5P18Var4

"""
THINGS TO NOTE ABOUT THIS PROBLEM

"""


class Problem5P18Var4Vlad(Problem5P18Var4):
    def spiral_order_of_non_sqr_matrix(self, non_sqr_matrix):
        return self.modified_single_step_book_soln(non_sqr_matrix)

    # same idea as book solution but now we just need to separate row and column dimensions
    def modified_single_step_book_soln(self, non_sqr_matrix):
        shift = ((0, 1), (1, 0), (0, -1), (-1, 0))
        spiral_ordered_list = []
        x = y = 0
        direction = 0
        for _ in range(len(non_sqr_matrix) * len(non_sqr_matrix[0])):
            spiral_ordered_list.append(non_sqr_matrix[x][y])
            non_sqr_matrix[x][y] = 0
            next_x, next_y = x + shift[direction][0], y + shift[direction][1]
            if next_x == len(non_sqr_matrix) or next_y == len(non_sqr_matrix[0]) or non_sqr_matrix[next_x][next_y] == 0:
                direction = (direction + 1) & 3
                next_x, next_y = x + shift[direction][0], y + shift[direction][1]
            x, y = next_x, next_y
        return spiral_ordered_list


