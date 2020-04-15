from protocol.problem_5_p_6_var1 import Problem5P6Var1

"""
THINGS TO NOTE ABOUT THIS PROBLEM

"""


class Problem5P6Var1Vlad(Problem5P6Var1):
    def find_longest_equal_sublist(self, int_list):
        # return self.brute_force(int_list)
        return self.one_pass(int_list)

    def brute_force(self, int_list):
        longest_sublist = 0
        for i in range(len(int_list)):
            curr_longest_sublist = 0
            j = i
            while int_list[j] == int_list[i]:
                curr_longest_sublist += 1
                j += 1
                if j == len(int_list):
                    break
            longest_sublist = max(longest_sublist, curr_longest_sublist)
        return longest_sublist

    def one_pass(self, int_list):
        longest_sublist = 1
        prev_val = None
        curr_longest_sublist = 1
        for val in int_list:
            if val == prev_val:
                curr_longest_sublist += 1
            else:
                curr_longest_sublist = 1
            longest_sublist = max(longest_sublist, curr_longest_sublist)
            prev_val = val
        return longest_sublist



