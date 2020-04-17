from protocol.problem_6_p_4 import Problem6P4

"""
THINGS TO NOTE ABOUT THIS PROBLEM
"""


class Problem6P4Vlad(Problem6P4):
    def replace_and_remove(self, str_list, size):
        self.three_pass(str_list, size)
        # self.book_solution(str_list, size)

    def three_pass(self, str_list, size):
        # first delete all the 'b's and count num of 'a's - 'b's to get final string length
        num_as = num_bs = 0
        for i in range(size):
            if str_list[i] == 'b':
                str_list[i] = '-'
                num_bs += 1
            elif str_list[i] == 'a':
                num_as += 1
        final_string_len = size + num_as - num_bs

        # shift all elements as left as possible
        start_ptr = after_start_ptr = 0
        while after_start_ptr < len(str_list):
            if str_list[start_ptr] == '-' and str_list[after_start_ptr] != '-':
                str_list[start_ptr], str_list[after_start_ptr] = str_list[after_start_ptr], str_list[start_ptr]
                start_ptr += 1
            elif str_list[start_ptr] != '-':
                start_ptr += 1
            after_start_ptr += 1


        # build array from end to start while keeping two pointers to keep track of last inserted element and current
        # list element of interest
        end_ptr = before_end_ptr = final_string_len - 1
        while before_end_ptr != -1:
            if str_list[before_end_ptr] != '-':
                if str_list[before_end_ptr] == 'a':
                    str_list[end_ptr], str_list[end_ptr - 1] = 'd', 'd'
                    end_ptr = end_ptr - 2
                else:
                    str_list[end_ptr] = str_list[before_end_ptr]
                    end_ptr -= 1
            before_end_ptr -= 1

    def book_solution(self, str_list, size):
        write_idx = 0
        a_count = 0
        for i in range(size):
            if str_list[i] == 'a':
                a_count += 1
            if str_list[i] != 'b':
                str_list[i], str_list[write_idx] = str_list[write_idx], str_list[i]
                write_idx += 1

        cur_idx = write_idx - 1
        write_idx += a_count - 1
        final_size = write_idx
        while cur_idx >= 0:
            if str_list[cur_idx] == 'a':
                str_list[write_idx - 1: write_idx + 1] = ['d', 'd']
                write_idx -= 2
            else:
                str_list[cur_idx], str_list[write_idx] = str_list[write_idx], str_list[cur_idx]
                write_idx -= 1
            cur_idx -= 1
        return final_size



