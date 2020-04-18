from protocol.problem_8_p_1 import Problem8P1

"""
THINGS TO NOTE ABOUT THIS PROBLEM

"""


class Problem8P1Vlad(Problem8P1):
    class StackWithMax(Problem8P1.StackWithMax):
        def __init__(self, stack_vals=None):
            self.stack = []
            self.create_stack(stack_vals)

        def create_stack(self, stack_vals):
            if stack_vals:
                for val in stack_vals:
                    self.push(val)

        def get_max(self):
            return self.peek().max if self.peek() else None

        def push(self, val):
            max_val = max(val, self.get_max()) if self.stack else val
            elem = StackElem(val, max_val)
            self.stack.append(elem)

        def pop(self):
            return self.stack.pop()

        def peek(self):
            return self.stack[-1] if self.stack else None

class StackElem(object):
    def __init__(self, val, max_val):
        self.val = val
        self.max = max_val   # this is the max of the current val and all stack valents below it
