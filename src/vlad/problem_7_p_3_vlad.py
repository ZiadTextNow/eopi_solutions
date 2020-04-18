from protocol.problem_7_p_3 import Problem7P3
from protocol.problem_7_p_1 import ListNode

"""
THINGS TO NOTE ABOUT THIS PROBLEM

Floyds algo is really cool!
problem 7.3var1 is not correct. Proven by contradiction. If length till cycle start is a and cycle length is c and where
slow and fast pointer meet of the cycle relative to cycle start a is p. Then is a = 2, c = 3, and p = 0 then the 
solution 7.3var1 would return that node at index 3 but the correct answer is node at index 2
"""


class Problem7P3Vlad(Problem7P3):
    def check_for_llist_cycle(self, llist_a):
        return self.floyds_algo(llist_a)

    def floyds_algo(self, llist_a):
        normal_ptr = fast_ptr = llist_a
        # check if there is a cycle
        while True:
            normal_ptr = normal_ptr.next
            if fast_ptr.next and fast_ptr.next.next:
                fast_ptr = fast_ptr.next.next
            else:
                return None
            if normal_ptr == fast_ptr:
                break
        # get the cycle length
        intercept = cycle_ptr = normal_ptr
        cycle_length = 0
        while True:
            cycle_ptr = cycle_ptr.next
            cycle_length += 1
            if cycle_ptr == intercept:
                break
        # find the start of the cycle
        start_ptr = offset_ptr = llist_a
        for _ in range(cycle_length):
            offset_ptr = offset_ptr.next
        while start_ptr != offset_ptr:
            start_ptr, offset_ptr = start_ptr.next, offset_ptr.next
        return start_ptr




