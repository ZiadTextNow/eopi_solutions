from protocol.errors import EOPINotImplementedError
from protocol.problem_7_p_1 import LinkedList


class Problem7P3(object):
    def check_for_llist_cycle(self, llist_a):
        raise EOPINotImplementedError()


class LinkedList(LinkedList):
    def make_loop(self, node_idx):
        # nodes begin from index 1
        loop_node = self.get_node_at_idx(node_idx)
        self.tail.next = loop_node

    def get_node_at_idx(self, node_idx):
        # nodes begin from index 1
        node_at_idx = self.head
        for _ in range(1, node_idx):
            node_at_idx = node_at_idx.next
        return node_at_idx


