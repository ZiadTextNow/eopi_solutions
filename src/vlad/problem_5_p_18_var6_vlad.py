from protocol.problem_5_p_18_var6 import Problem5P18Var6

"""
THINGS TO NOTE ABOUT THIS PROBLEM

I believe second answer from here:
https://stackoverflow.com/questions/54774747/compute-the-kth-element-in-spiral-order-for-an-m-x-n-2d-array-a-in-o1-time
is correct. It's mainly a math problem and after having spent very long doing my solution below which does not work I 
decided to move on and maybe come back to this later.
"""


class Problem5P18Var6Vlad(Problem5P18Var6):
    def kth_elem_spiral_order(self, non_sqr_matrix, k):
        return self.constant_lookup(non_sqr_matrix, k)

    """
    Things we know:
    if num_rows != 1 or num_columns != 1 then perimeter length is num_rows * 2 + num_columns * 2 - 4
    if num_rows == 1 or num_columns == 1 then perimeter len
    if num_rows > 1 and num_columns > 1 then perimeter length of a shell is previous perimeter length + 8 
    if num_rows == 1 or num_columns == 1 then perimeter length of a shell is num_rows * 2 + num_columns * 2 + 4 
    """
    def constant_lookup(self, non_sqr_matrix, k):
        num_rows = len(non_sqr_matrix)
        num_columns = len(non_sqr_matrix[0])

        # define base size
        if num_rows & 1 and num_rows >= 3:
            num_base_rows = 3
        elif not num_rows & 1 and num_rows > 3:
            num_base_rows = 2
        else:
            num_base_rows = num_rows
        if num_columns & 1 and num_columns >= 3:
            num_base_columns = 3
        elif not num_columns & 1 and num_columns > 3:
            num_base_columns = 2
        else:
            num_base_columns = num_columns

        # if k is bigger than area of base size then check which shell it's in
        area = num_base_rows * num_base_columns
        if k > area:
            num_shells = (k - area) // 8 + 1
        else:
            num_shells = 0

        k = (k - area)

        # amount with shells included
        num_shell_rows = num_base_rows + num_shells * 2
        num_shell_columns = num_base_columns + num_shells * 2

        row_diff = num_rows - num_shell_rows
        column_diff = num_columns - num_shell_columns
        # this is the exact index finder in that shell
        if k < num_shell_columns:
            row = row_diff / 2
            column = column_diff / 2 + k
        elif k < num_shell_columns + num_shell_rows - 1:
            row = row_diff / 2 + (k + 1 - num_shell_columns)
            column = column_diff / 2 + num_shell_columns - 1
        elif k < num_shell_columns * 2 + num_shell_rows - 2:
            row = row_diff / 2 + num_shell_rows - 1
            column = column_diff / 2 + (num_shell_columns - 1 - (k + 1 - (num_shell_columns + num_shell_columns - 1)))
        elif k < num_shell_columns * 2 + num_shell_rows * 2 - 4:
            row = row_diff / 2 + num_shell_rows - (k + 1 - (num_shell_columns * 2 + num_shell_rows - 2))
            column = column_diff / 2
        return non_sqr_matrix[int(row)][int(column)]



        # while 1:
        #     if num_rows == 1 and num_columns == 1:
        #         perimeter_length = 1
        #     else:
        #         perimeter_length = num_rows * 2 + num_columns * 2 - 4
        #     if k < perimeter_length:
        #         pass
        #     k -= perimeter_length
