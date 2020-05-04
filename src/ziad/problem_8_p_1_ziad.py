from protocol.problem_8_p_1 import Problem8P1

'''
    NOTE: I have implemented 4 separate approaches
        1. Brute force
        2. more elegant - reserve extra memory for a variable that keeps track of max (i.e. stateless max)
        3. even better - use a list of tuples!
        4. Two stack approach - maintain another stack for max values (i.e. stateful max)     
'''


class Problem8P1Ziad(Problem8P1):
    class StackWithMax(Problem8P1.StackWithMax):
        def __init__(self, stack_vals=None):
            # brute force approach
            # self.values = []
            # self.values.append(first_elem)

            # more elegant - reserve extra memory for a variable that keeps track of max (i.e. stateless max)
            # self.max_so_far = first_elem if first_elem else None

            # even better -> list of tuples!
            # self.values_with_cached_max = [(first_elem, first_elem)]
            self.values_with_cached_max = []
            self.create_stack(stack_vals)

            # Two-Stack approach - maintain another stack for max values (i.e. stateful max)
            # self.max_values = []

        # Adapted from Vlad's API
        def create_stack(self, stack_vals):
            if stack_vals:
                for val in stack_vals:
                    self.push(val)

        def max(self):
            # brute force
            # return self.__naive_max()

            # more elegant
            # return self.max_so_far

            # even better - list of tuples
            return self.peek()[1]

            # two stacks
            # return self.max_values[-1]

        def push(self, elem):
            # self.values.append(elem)

            # brute force
            # self.max_so_far = self.__naive_max()

            # more elegant - update max_so_far if needed
            # self.max_so_far = max(self.max_so_far, elem)

            # even better - using a list of tuples
            self.values_with_cached_max.append((elem, max(elem, self.peek()[1])))

            # Two stacks Approach
            # self.values.append(elem)
            # if len(self.values) == 1:
            #     self.max_values.append(elem)
            #     return
            #
            # if elem > self.max_values[-1]:
            #     self.max_values.append(elem)
            # else:
            #     self.max_values.append(self.max_values[-1])

        def pop(self):
            # brute force
            # popped = self.values.pop()
            # self.max_so_far = self.__naive_max()

            # even better - list of tuples!
            popped = self.values_with_cached_max.pop()

            # Two stacks
            # popped = self.values.pop()
            # del self.max_values[-1]

            return popped

        def is_empty(self):
            # brute force
            # return len(self.values) == 0

            # even better - list of tuples
            return len(self.values_with_cached_max) == 0

            # Two Stack Approach
            # return not self.values_with_cached_max

        def peek(self):
            return self.values_with_cached_max[-1]

        # Helper function
        def pretty_print(self):
            if self.is_empty():
                print("Stack is empty")
            else:
                # print(self.values)
                print(self.values_with_cached_max)

        # Helper function for the brute force approach
        def __naive_max(self):
            if self.is_empty():
                self.pretty_print()
            else:
                max_so_far = self.values[0]
                for elem in self.values:
                    max_so_far = max(max_so_far, elem)
                return max_so_far
