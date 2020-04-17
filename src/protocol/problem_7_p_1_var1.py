from protocol.errors import EOPINotImplementedError


class Problem7P1Var1(object):
    def merge_two_sorted_dllists(self, dllist_a, dllist_b):
        raise EOPINotImplementedError()


class ListNode(object):
    def __init__(self, data=None, next_node=None, previous=None):
        self.data = data
        self.next = next_node
        self.previous =previous


class DoublyLinkedList(object):
    def __init__(self, list_elements):
        self.head = self.create_linked_list(list_elements)

    def create_linked_list(self, list_elements):
        if not list_elements:
            return None
        head = cur_node = ListNode(list_elements[0])
        for i in range(1, len(list_elements)):
            new_node = ListNode(list_elements[i])
            cur_node.next = new_node
            new_node.previous = cur_node
            cur_node = new_node
        cur_node.next = None
        return head

    def search_list(self, key):
        list_iterator = self.head
        while list_iterator.data != key:
            list_iterator = list_iterator.next
        return list_iterator

    def insert_node_after(self, new_node, node):
        new_node.next = node.next
        new_node.previous = node
        node.next.previous = new_node
        node.next = new_node

    def delete_node_after(self, node):
        node.next = node.next.next
        node.next.previous = node
