from protocol.problem_15_p_2 import Problem15P2

"""
THINGS TO NOTE ABOUT THIS PROBLEM

passing in copies of list is so important instead of references!

You can eliminate single if statements within for loops by using if all()

a for loop such as the one used in book solution can be illuminated by 
passing in another argument to the recursive function that you increment 
yourself

for recursive questions like this where you need to continously build up and 
maintain a list of current result. Instead of appending to a new copy of the 
list you can make the cur_list of exact size at the beginning and set values 
by exact indices such as using row index in this example!
"""


class Problem15P2Vlad(Problem15P2):
    def non_attacking_placements_of_n_queens(self, n):
        # return self.try_all_columns(n)
        return self.try_all_columns_less_memory(n)

    """
    so we know since the board is n x n and we need to place n queens there must
    be exactly 1 queen in each row. Also, must be exactly 1 queen in each column
    and can not attack each other diagonally. We can store the queen column
    postion in a list were list indices are the row numbers. Rows and columns
    start from index 0
    """
    def try_all_columns(self, n):
        def safe_to_place(placements, cur_colm):
            cur_row = len(placements)
            # for row, colm in enumerate(placements):
            #     if abs(cur_colm - colm) == abs(cur_row - row) or cur_colm == \
            #             colm:
            #         return False
            # return True

            # above loop can be rewritten using all to remove inner if
            if all(abs(cur_colm - colm) != abs(cur_row - row) and
                   cur_colm != colm
                   for row, colm in enumerate(placements)):
                return True
            return False

        def inner_func(cur_placements, cur_colm):
            if len(cur_placements) == n:
                final_placements.append(cur_placements)
            elif cur_colm < n:
                if safe_to_place(cur_placements, cur_colm):
                    # make a copy of the cur_placements since it might be appended
                    cur_placements_copy = list(cur_placements)
                    # this append is why we made a copy above
                    cur_placements.append(cur_colm)
                    inner_func(cur_placements, 0)
                    cur_placements = cur_placements_copy
                cur_colm += 1
                # this always happens even if it can be placed to not miss any
                # possibilities
                inner_func(cur_placements, cur_colm)
        final_placements = []
        inner_func([], 0)
        distinct_final_placements = []
        for cur_placements in final_placements:
            if cur_placements not in distinct_final_placements:
                distinct_final_placements.append(cur_placements)

        return [[(row, colm) for row, colm in enumerate(cur_placements)]
                for cur_placements in distinct_final_placements]


    def try_all_columns_less_memory(self, n):
        def safe_to_place(cur_row, cur_colm):
            if all(abs(cur_colm - colm) != abs(cur_row - row) and
                   cur_colm != colm
                   for row, colm in enumerate(cur_placements[:cur_row])):
                return True
            return False

        def inner_func(cur_row, cur_colm):
            if cur_row == n:
                # make sure you actually make a copy of the list!!!!!!!!!!
                final_placements.append(list(cur_placements))
            elif cur_colm < n:
                if safe_to_place(cur_row, cur_colm):
                    cur_placements[cur_row] = cur_colm
                    inner_func(cur_row+1, 0)
                inner_func(cur_row, cur_colm+1)

        final_placements = []
        cur_placements = [0] * n
        inner_func(0, 0)

        distinct_final_placements = []
        for cur_placements in final_placements:
            if cur_placements not in distinct_final_placements:
                distinct_final_placements.append(cur_placements)

        return [[(row, colm) for row, colm in enumerate(cur_placements)]
                for cur_placements in distinct_final_placements]
