from protocol.problem_8_p_1 import Problem8P1


class Problem8P1Arshan(Problem8P1):
    class ListNode:
        def __init__(self):
            self.value = None
            self.next = None

    class StackWithMaxLinkedList(object):
        def __init__(self, vals=None):
            self.head = None
            self.tail = None
            self.max_val = None
            if vals:
                for v in vals:
                    self.push(v)

        def max(self):
            if self.is_empty():
                raise IndexError
            return self.max_val

        def push(self, elem):
            new_node = Problem8P1Arshan.ListNode()
            new_node.value = elem
            new_node.next = self.head
            if self.max_val:
                self.max_val = max(self.max_val, new_node.value)
            else:
                self.max_val = new_node.value
            self.head = new_node

        def pop(self):
            if self.is_empty():
                raise IndexError
            val = self.head.value
            self.head = self.head.next
            if val == self.max_val:
                self.max_val = self.find_max()
            return val

        def find_max(self):
            it = self.head
            m = None
            while it:
                if not m:
                    m = it.value
                m = max(m, it.value)
                it = it.next
            return m

        def is_empty(self):
            return self.max_val is None

    class StackWithMax(StackWithMaxLinkedList):
        pass
