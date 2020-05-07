from protocol.problem_8_p_1 import Problem8P1


class Problem8P1Arshan(Problem8P1):
    class ListNode:
        def __init__(self):
            self.value = None
            self.next = None

    class StackWithMaxNormalList(object):
        def __init__(self, vals=None):
            self.stack = vals or []
            self.maxes = []

        def _check_empty(self):
            if not self.maxes:
                raise IndexError("Stack is empty")

        def max(self):
            self._check_empty()
            return self.maxes[-1][0]

        def push(self, elem):
            if not self.stack:
                self.maxes.append((elem, 1))
            else:
                self._add_new_max(elem)
            self.stack.append(elem)

        def _add_new_max(self, new_max):
            curr_max, curr_count = self.maxes[-1]
            if new_max > curr_max:
                self.maxes.append((new_max, 1))
            elif new_max == curr_max:
                self.maxes[-1] = (
                    curr_max,
                    curr_count + 1
                )

        def _pop_max(self):
            curr_max, count = self.maxes[-1]
            count -= 1
            if count:
                self.maxes[-1] = (curr_max, count)
            else:
                self.maxes.pop()
            return curr_max

        def pop(self):
            self._check_empty()
            if self.stack[-1] == self.max():
                return self._pop_max()
            return self.stack.pop()

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
