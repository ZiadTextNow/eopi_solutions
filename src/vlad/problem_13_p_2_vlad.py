from protocol.problem_13_p_2 import Problem13P2

"""
THINGS TO NOTE ABOUT THIS PROBLEM

"""


class Problem13P2Vlad(Problem13P2):
    def merge_two_sorted_lists(self, sorted_list_a, sorted_list_b):
        # return self.merge_than_sort(sorted_list_a, sorted_list_b)
        return self.fill_from_the_rear(sorted_list_a, sorted_list_b)

    def merge_than_sort(self, sorted_list_a, sorted_list_b):
        num_of_list_a_elems = 0
        while sorted_list_a[num_of_list_a_elems] != '_':
            num_of_list_a_elems += 1
        sorted_list_a[num_of_list_a_elems: num_of_list_a_elems + len(sorted_list_b)] = sorted_list_b
        sorted_list_a = sorted(sorted_list_a[:num_of_list_a_elems + len(sorted_list_b)]) + \
            sorted_list_a[num_of_list_a_elems + len(sorted_list_b):]
        return sorted_list_a

    def fill_from_the_rear(self, sorted_list_a, sorted_list_b):
        def get_num_of_list_a_elems():
            num_of_list_a_elems = 0
            while sorted_list_a[num_of_list_a_elems] != '_':
                num_of_list_a_elems += 1
            return num_of_list_a_elems

        num_of_list_a_elems = get_num_of_list_a_elems()
        end_ptr = num_of_list_a_elems + len(sorted_list_b) - 1
        list_a_ptr = num_of_list_a_elems - 1
        list_b_ptr = len(sorted_list_b) - 1
        while list_a_ptr >= 0 and list_b_ptr >= 0:
            if sorted_list_b[list_b_ptr] > sorted_list_a[list_a_ptr]:
                sorted_list_a[end_ptr] = sorted_list_b[list_b_ptr]
                list_b_ptr -= 1
            else:
                sorted_list_a[end_ptr] = sorted_list_a[list_a_ptr]
                list_a_ptr -= 1
            end_ptr -= 1
        if list_b_ptr >= 0:
            sorted_list_a[:end_ptr + 1] = sorted_list_b[:list_b_ptr + 1]
        return sorted_list_a

    # this didn't work :(
    def three_ptr_shit(self, sorted_list_a, sorted_list_b):
        def get_num_of_list_a_elems(list_a):
            num_of_list_a_elems = 0
            while sorted_list_a[num_of_list_a_elems] != '_':
                num_of_list_a_elems += 1
            return num_of_list_a_elems

        num_of_list_a_elems = get_num_of_list_a_elems(sorted_list_a)
        first_ptr = 0
        second_ptr = third_ptr = num_of_list_a_elems
        list_b_ptr = 0
        while sorted_list_b[list_b_ptr] > sorted_list_a[first_ptr]:
            first_ptr += 1
        sorted_list_a[third_ptr] = sorted_list_a[first_ptr]
        third_ptr += 1
        sorted_list_a[first_ptr] = sorted_list_b[list_b_ptr]
        first_ptr += 1
        list_b_ptr += 1
        while list_b_ptr < len(sorted_list_b):
            if sorted_list_a[first_ptr] > sorted_list_b[list_b_ptr] and sorted_list_b[second_ptr] > sorted_list_b[list_b_ptr]:
                sorted_list_a[third_ptr] = sorted_list_a[first_ptr]
                if first_ptr == second_ptr:   # this resets the second ptr
                    second_ptr = third_ptr
                third_ptr += 1
                sorted_list_a[first_ptr] = sorted_list_b[list_b_ptr]
                first_ptr += 1
                list_b_ptr += 1
            elif first_ptr == second_ptr:   # keep moving both ptrs till above if statement is true
                first_ptr += 1
                second_ptr += 1
            elif sorted_list_a[second_ptr] <= sorted_list_b[list_b_ptr]:
                sorted_list_a[third_ptr] = sorted_list_a[first_ptr]
                third_ptr += 1
                sorted_list_a[first_ptr] = sorted_list_a[second_ptr]
                second_ptr += 1
                first_ptr += 1
            elif sorted_list_a[first_ptr] <= sorted_list_b[list_b_ptr]:
                first_ptr += 1

        # we have finished going through list_b. Now all we have to do is rotate first_ptr about second_ptr
        while first_ptr < second_ptr:
            sorted_list_a[third_ptr] = sorted_list_a[first_ptr]
            sorted_list_a[first_ptr] = sorted_list_a[second_ptr]


