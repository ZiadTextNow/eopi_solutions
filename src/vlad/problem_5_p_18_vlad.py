from protocol.problem_5_p_18 import Problem5P18
import math

"""
THINGS TO NOTE ABOUT THIS PROBLEM

"""


class Problem5P18Vlad(Problem5P18):
    def spiral_ordering(self, two_d_list):
        # return self.iterative_walk(two_d_list)
        return self.single_step_book_soln(two_d_list)

    # after looking at book solution realized could've used -1 instead of len(two_d_list) - 1 for getting last list elem
    def iterative_walk(self, two_d_list):
        spiral_ordered_list = []
        trans_list = list(map(list, zip(*two_d_list)))  # save a copy of a transposed list since it's commonly used
        for i in range(math.ceil(len(two_d_list) / 2)):
            last_idx = len(two_d_list) - 1 - i
            if last_idx - i == 0:   # this handles the case when len(two_d_list) is odd and it's time to add center val
                spiral_ordered_list += [two_d_list[i][i]]
            top_row = two_d_list[i][i:last_idx]
            right_column = trans_list[last_idx][i: last_idx]
            bottom_row = two_d_list[last_idx][last_idx:i: -1]
            left_column = trans_list[i][last_idx:i: -1]
            spiral_ordered_list = spiral_ordered_list + top_row + right_column + bottom_row + left_column
        return spiral_ordered_list

    def single_step_book_soln(self, two_d_list):
        shift = ((0, 1), (1, 0), (0, -1), (-1, 0))
        spiral_ordered_list = []
        x = y = 0
        direction = 0
        for _ in range(len(two_d_list)**2):
            spiral_ordered_list.append(two_d_list[x][y])
            two_d_list[x][y] = 0
            next_x, next_y = x + shift[direction][0], y + shift[direction][1]
            if next_x == len(two_d_list) or next_y == len(two_d_list) or two_d_list[next_x][next_y] == 0:
                direction = (direction + 1) & 3
                next_x, next_y = x + shift[direction][0], y + shift[direction][1]
            x, y = next_x, next_y
        return spiral_ordered_list


