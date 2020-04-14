from protocol.problem_5_p_1_var4 import Problem5P1Var4

"""
THINGS TO NOTE ABOUT THIS PROBLEM

This method was not used in problem 5.1var3 since this always goes through the entire list with one pointer and the 
other traverses part of the list. In the solution in 5.1var3 both pointers together only travers list once

"""


class Problem5P1Var4Vlad(Problem5P1Var4):
    def bool_val_keep_true_order_partition(self, unpartitioned_list):
        self.same_end_double_ptr_partition(unpartitioned_list)

    # Traverse from end to start keeping two pointers, this guarantees and new true value is kept in order
    def same_end_double_ptr_partition(self, unpartitioned_list):
        end_ptr = len(unpartitioned_list) - 1
        for before_end_ptr in reversed(range(len(unpartitioned_list))):
            if unpartitioned_list[before_end_ptr]:
                unpartitioned_list[before_end_ptr], unpartitioned_list[end_ptr] = unpartitioned_list[end_ptr], \
                                                                                  unpartitioned_list[before_end_ptr]
                end_ptr -= 1
