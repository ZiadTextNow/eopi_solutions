from protocol.problem_5_p_1_var1 import Problem5P1Var1
from vlad.problem_5_p_1_vlad import Problem5P1Vlad

"""
THINGS TO NOTE ABOUT THIS PROBLEM

The dutch partition method can be generally applied to any 3 distinct groups that you define. The pivot was just a 
a technique of doing so in prob5.1 by using values < = > pivot while here we use three exact values!

"""


class Problem5P1Var1Vlad(Problem5P1Var1):
    def three_val_partition(self, unpartitioned_list):
        # return self.using_dutch_flag_partition(unpartitioned_list)
        return self.modified_dutch_flag_partition(unpartitioned_list)

    # I'm impressed this worked!
    def modified_dutch_flag_partition(self, unpartitioned_list):
        first_val = unpartitioned_list[0]
        first_ptr = 0
        second_val = None
        second_ptr = len(unpartitioned_list) - 1
        unknown_ptr = 0
        while unknown_ptr <= second_ptr:
            if unpartitioned_list[unknown_ptr] == first_val:
                unpartitioned_list[first_ptr], unpartitioned_list[unknown_ptr] = unpartitioned_list[unknown_ptr], \
                                                                                 unpartitioned_list[first_ptr]
                first_ptr += 1
                unknown_ptr += 1
            # only modification required to set the second_val since we don't know what it is at the start
            elif second_val is None:
                second_val = unpartitioned_list[unknown_ptr]
            elif unpartitioned_list[unknown_ptr] == second_val:
                unpartitioned_list[second_ptr], unpartitioned_list[unknown_ptr] = unpartitioned_list[unknown_ptr], \
                                                                                  unpartitioned_list[second_ptr]
                second_ptr -= 1
            else:
                unknown_ptr += 1
        print(unpartitioned_list)

    def using_dutch_flag_partition(self, unpartitioned_list):
        pivot = self.find_mid_val(unpartitioned_list)  # set the pivot to the middle value of the three values
        Problem5P1Vlad().one_pass_dutch_flag_partition(pivot, unpartitioned_list)  # Now it's the same as before!

    def find_mid_val(self, unpartitioned_list):
        min_val = mid_val = max_val = unpartitioned_list[0]
        for val in unpartitioned_list:
            # checks are kinda messy feel like there is simpler way to do this
            if val > max_val:
                mid_val = max_val
                max_val = val
            elif val < min_val:
                mid_val = min_val
                min_val = val
            elif val > min_val and val < max_val:
                mid_val = val
        return mid_val




