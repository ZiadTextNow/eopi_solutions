from protocol.problem_7_p_1_var1 import Problem7P1Var1
from protocol.problem_7_p_1_var1 import ListNode


class Problem7P1Var1Ziad(Problem7P1Var1):
    def merge_two_sorted_dllists(self, dllist_a, dllist_b):
        return self.merge(dllist_a, dllist_b)

    # time: O(n)
    # space: O(m + n)
    def merge(self, list_1, list_2):
        dummy_node = ListNode()
        merged_list = dummy_node

        while list_1 and list_2:
            if list_1.data <= list_2.data:
                dummy_node.next = list_1
                list_1.previous = dummy_node
                list_1 = list_1.next
            else:
                dummy_node.next = list_2
                list_2.previous = dummy_node
                list_2 = list_2.next

            dummy_node = dummy_node.next

        if list_1:
            dummy_node.next = list_1
            dummy_node.next.previous = dummy_node
        if list_2:
            dummy_node.next = list_2
            dummy_node.next.previous = dummy_node

        return merged_list.next
