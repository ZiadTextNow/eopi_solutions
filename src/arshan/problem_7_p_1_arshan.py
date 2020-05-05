from protocol.problem_7_p_1 import LinkedList, ListNode


class Problem7P1Arshan(object):
    def merge_two_sorted_llists(self, it_a: ListNode, it_b: ListNode):
        merged = LinkedList([])
        while (it_a is not None) or (it_b is not None):
            if it_a is None:
                merged.push_back(it_b.data)
                it_b = it_b.next
                continue
            if it_b is None:
                merged.push_back(it_a.data)
                it_a = it_a.next
                continue
            if it_a.data > it_b.data:
                merged.push_back(it_b.data)
                it_b = it_b.next
            else:
                merged.push_back(it_a.data)
                it_a = it_a.next
        return merged.head
