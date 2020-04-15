from protocol.problem_5_p_18_var5 import Problem5P18Var5

"""
THINGS TO NOTE ABOUT THIS PROBLEM

"""


class Problem5P18Var5Vlad(Problem5P18Var5):
    def last_elem_spiral_order(self, non_sqr_matricolumn):
        return self.constant_lookup(non_sqr_matricolumn)

    # this is some weird math thing I thought of that works in constant time and is kinda messy
    def constant_lookup(self, non_sqr_matricolumn):
        num_rows = len(non_sqr_matricolumn)
        num_columns = len(non_sqr_matricolumn[0])
        if num_columns >= num_rows:
            column_offset = (num_rows - 1) // 2
            row_offset = (num_rows - 1) // 2
            if num_rows & 1:
                column = num_columns - 1 - column_offset
            else:
                column = column_offset
            if num_rows & 1:
                row = row_offset
            else:
                row = num_rows - 1 - row_offset

        else:
            column_offset = (num_columns - 1) // 2
            row_offset = num_columns // 2
            if num_columns & 1:
                column = num_columns - 1 - column_offset
            else:
                column = column_offset
            if num_columns & 1:
                row = num_rows - 1 - row_offset
            else:
                row = row_offset
        return non_sqr_matricolumn[row][column]

