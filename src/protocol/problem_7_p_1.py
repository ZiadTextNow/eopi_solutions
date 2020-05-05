from protocol.errors import EOPINotImplementedError


class Problem7P1(object):
    def merge_two_sorted_llists(self, llist_a, llist_b):
        raise EOPINotImplementedError()


"""
not sure if both these classes below should be implemented here. The rationale was that these are essential to solving
the problem ,but are not part of the actual problem. They are used in the test cases and since we share test cases I 
didn't find it right for the test case to import from say problem_7_p_1_vlad since that is a solution specific to me. 
"""


class ListNode(object):
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList(object):
    def __init__(self, list_elements):
        self.head, self.tail = self.create_linked_list(list_elements)

    def create_linked_list(self, list_elements) -> (ListNode, ListNode):
        if not list_elements:
            return None, None
        head = cur_node = ListNode(list_elements[0])
        for i in range(1, len(list_elements)):
            new_node = ListNode(list_elements[i])
            cur_node.next = new_node
            cur_node = new_node
        cur_node.next = None
        tail = cur_node
        return head, tail

    def push(self, key):
        new_head = ListNode(key, self.head)
        self.head = new_head

    def push_back(self, key):
        new_tail = ListNode(key)
        if not self.tail:
            self.head = self.tail = new_tail
        self.tail.next = new_tail
        self.tail = new_tail

    def search_list(self, key):
        list_iterator = self.head
        while list_iterator.data != key:
            list_iterator = list_iterator.next
        return list_iterator

    def insert_node_after(self, new_node, node):
        new_node.next = node.next
        node.next = new_node

    def delete_node_after(self, node):
        node.next = node.next.next

    def to_list(self):
        output = []
        node = self.head
        while node:
            output.append(node.data)
            node = node.next
        return output
