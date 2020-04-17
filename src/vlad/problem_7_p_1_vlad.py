from protocol.problem_7_p_1 import Problem7P1
from protocol.problem_7_p_1 import ListNode

"""
THINGS TO NOTE ABOUT THIS PROBLEM
"""


class Problem7P1Vlad(Problem7P1):
    def merge_two_sorted_llists(self, llist_a, llist_b):
        return self.simultaneous_list_walk(llist_a, llist_b)

    # did same as book but book did it way cleaner
    def simultaneous_list_walk(self, llist_a, llist_b):
        start_node = sorted_llist = ListNode()
        while 1:
            if llist_a and llist_b:
                if llist_a.data < llist_b.data:
                    sorted_llist.next, llist_a = llist_a, llist_a.next
                else:
                    sorted_llist.next, llist_b = llist_b, llist_b.next
                sorted_llist = sorted_llist.next
            # these elif could've been nicely cleaned up with llist_a or llist_b like the book
            elif llist_a:
                sorted_llist.next = llist_a
                break
            elif llist_b:
                sorted_llist.next = llist_b
                break
        return start_node.next
