from protocol.problem_7_p_1 import Problem7P1
from protocol.problem_7_p_1 import ListNode


class Problem7P1Ziad(Problem7P1):
    def merge_two_sorted_llists(self, llist_a, llist_b):
        # return self.naive_merge(llist_a, llist_b)
        return self.better_merge(llist_a, llist_b)

    # Brute force approach
    # just append list_2 to list_1 and sort the resulting list
    # time: O(m + n)
    # space: O(1)
    def naive_merge(self, list_1, list_2):
        # solved in EOPI so I won't rewrite it here
        return

    # A more time-efficient approach
    # Keep iterating until you have both list pointers are None (i.e. you have reached the end of both lists)
    # time: O(n) where n is the length of the shorter of the two lists
    # space: O(m + n) for the newly allocated list
    def better_merge(self, list_1, list_2):
        # optimization: early-return in the edge case that one of the two lists is empty
        if not list_1:
            return list_2

        if not list_2:
            return list_1

        dummy_node = ListNode()
        merged_list = dummy_node

        while list_1 and list_2:
            if list_1.data <= list_2.data:
                dummy_node.next = list_1
                list_1 = list_1.next
            else:
                merged_list.data = list_2.data
                list_2 = list_2.next

            dummy_node = dummy_node.next

        if list_1:
            dummy_node.next = list_1
        if list_2:
            dummy_node.next = list_2

        return merged_list.next
