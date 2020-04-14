from protocol.problem_5_p_1_var3 import Problem5P1Var3

"""
THINGS TO NOTE ABOUT THIS PROBLEM

"""


class Problem5P1Var3Vlad(Problem5P1Var3):
    def bool_val_partition(self, unpartitioned_list):
        self.two_end_ptr_partition(unpartitioned_list)

    def two_end_ptr_partition(self, unpartitioned_list):
        start_ptr = 0
        end_ptr = len(unpartitioned_list) - 1
        while start_ptr < end_ptr:
            if not unpartitioned_list[start_ptr]:
                start_ptr += 1
            elif unpartitioned_list[end_ptr]:
                end_ptr -= 1
            else:
                unpartitioned_list[start_ptr], unpartitioned_list[end_ptr] = unpartitioned_list[end_ptr], unpartitioned_list[start_ptr]
                start_ptr, end_ptr = start_ptr + 1, end_ptr - 1

