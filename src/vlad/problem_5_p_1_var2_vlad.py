from protocol.problem_5_p_1_var2 import Problem5P1Var2

"""
THINGS TO NOTE ABOUT THIS PROBLEM

Amazing how this dutch flag partition method works for partitioning a list of n distinct groups! Not just limited to 3
or 4. Although for larger n I can imagine there is a nicer iterative way of coding this

"""


class Problem5P1Var2Vlad(Problem5P1Var2):
    def four_val_partition(self, unpartitioned_list):
        return self.modified_dutch_flag_partition(unpartitioned_list)

    # I'm impressed this worked again!!!
    def modified_dutch_flag_partition(self, unpartitioned_list):
        start_val = unpartitioned_list[0]
        start_ptr = 0
        end_val = None
        end_ptr = len(unpartitioned_list) - 1
        before_end_val = None
        before_end_ptr = len(unpartitioned_list) - 1
        unknown_ptr = 0
        while unknown_ptr <= before_end_ptr:
            if unpartitioned_list[unknown_ptr] == start_val:
                unpartitioned_list[start_ptr], unpartitioned_list[unknown_ptr] = unpartitioned_list[unknown_ptr], \
                                                                                 unpartitioned_list[start_ptr]
                start_ptr += 1
                unknown_ptr += 1
            # only modification required is to set end_val and before_end_val since we don't know what it is at the start
            elif end_val is None:
                end_val = unpartitioned_list[unknown_ptr]
            elif before_end_val is None and unpartitioned_list[unknown_ptr] != end_val:
                before_end_val = unpartitioned_list[unknown_ptr]
            elif unpartitioned_list[unknown_ptr] == end_val:
                # Doing all three at once depends on the order you define them so I just wrote more verbose below
                # unpartitioned_list[end_ptr], unpartitioned_list[before_end_ptr], unpartitioned_list[unknown_ptr] = \
                #     unpartitioned_list[unknown_ptr], unpartitioned_list[end_ptr], unpartitioned_list[before_end_ptr]
                unpartitioned_list[end_ptr], unpartitioned_list[before_end_ptr] = unpartitioned_list[before_end_ptr], \
                                                                                unpartitioned_list[end_ptr]
                unpartitioned_list[end_ptr], unpartitioned_list[unknown_ptr] = unpartitioned_list[unknown_ptr], \
                                                                                  unpartitioned_list[end_ptr]
                end_ptr -= 1
                before_end_ptr -= 1
            elif unpartitioned_list[unknown_ptr] == before_end_val:
                unpartitioned_list[before_end_ptr], unpartitioned_list[unknown_ptr] = unpartitioned_list[unknown_ptr], \
                                                                                 unpartitioned_list[before_end_ptr]
                before_end_ptr -= 1
            else:
                unknown_ptr += 1
        print(unpartitioned_list)
