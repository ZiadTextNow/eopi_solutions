from protocol.errors import EOPINotImplementedError


class Problem7P1(object):
    def merge_two_sorted_llists(self, llist_a, llist_b):
        raise EOPINotImplementedError()


class ListNode(object):
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList(object):
    def __init__(self, list_elements):
        self.head, self.tail = self.create_linked_list(list_elements)

    def create_linked_list(self, list_elements):
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
