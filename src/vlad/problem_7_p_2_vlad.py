from protocol.problem_7_p_2 import Problem7P2
from protocol.problem_7_p_1 import ListNode

"""
THINGS TO NOTE ABOUT THIS PROBLEM

problem 7.2var1 is test case 3 and 7.2var2 is trivial using this same approach so they were not done :P 
"""


class Problem7P2Vlad(Problem7P2):
    def reverse_sublist(self, llist_a, s, f):
        return self.rotating_reverse(llist_a, s, f)

    def rotating_reverse(self, llist_a, s, f):
        llist_head = dummy_node = ListNode(next=llist_a)
        count = 1
        while count < s:
            dummy_node = dummy_node.next
            count += 1
        before_start_node, before_rotate_node, rotate_node = dummy_node, dummy_node.next, dummy_node.next.next
        while count < f:
            before_rotate_node.next = rotate_node.next
            rotate_node.next = before_start_node.next
            before_start_node.next = rotate_node
            rotate_node = before_rotate_node.next
            count += 1
        return llist_head.next


