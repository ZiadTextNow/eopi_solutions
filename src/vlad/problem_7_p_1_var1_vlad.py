from protocol.problem_7_p_1_var1 import Problem7P1Var1
from protocol.problem_7_p_1_var1 import ListNode

"""
THINGS TO NOTE ABOUT THIS PROBLEM

Very similar to singly linked list except the previous just needs to be updated but rather trivial
"""


class Problem7P1Var1Vlad(Problem7P1Var1):
    def merge_two_sorted_dllists(self, dllist_a, dllist_b):
        return self.simultaneous_list_walk(dllist_a, dllist_b)

    def simultaneous_list_walk(self, dllist_a, dllist_b):
        start_node = sorted_dllist = ListNode()
        while dllist_a and dllist_b:
            if dllist_a.data < dllist_b.data:
                sorted_dllist.next, dllist_a.previous, dllist_a = dllist_a, sorted_dllist, dllist_a.next
            else:
                sorted_dllist.next, dllist_b.previous, dllist_b = dllist_b, sorted_dllist, dllist_b.next
            sorted_dllist = sorted_dllist.next
        # appends remaining nodes
        sorted_dllist.next = dllist_a or dllist_b
        # this needed to be added for doubly linked list!
        sorted_dllist.next.previous = sorted_dllist
        return start_node.next
