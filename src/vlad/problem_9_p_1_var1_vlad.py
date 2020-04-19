from protocol.problem_9_p_1_var1 import Problem9P1Var1
import math

"""
THINGS TO NOTE ABOUT THIS PROBLEM

this is pretty clever but had to google to solve it. Don't really see how it's that similar to 9.1?
"""


class Problem9P1Var1Vlad(Problem9P1Var1):
    def largest_complete_subtree(self, binary_tree):
        return self.bottom_up_state_checker(binary_tree).size

    class ReturnType(object):
        def __init__(self, perfect=None, complete=None, size=0, root_node=None):
            self.perfect = perfect
            self.complete = complete
            self.size = size
            self.root_node = root_node

    """
    This only works for complete binary trees! logic is: if we call height h then complete tree is at least size
    2**(h-1) and at most 2**h - 1. if we add 1 we get 2**(h-1) + 1 and 2**h. If you take log2 of this range and then
    round up you will get h!!!
    """

    def size_to_height(self, size):
        return math.ceil(math.log2(size + 1))

    # I read over this below and then coded it from what I remembered! It's quite beautiful!
    # source: https://www.geeksforgeeks.org/find-the-largest-complete-subtree-in-a-given-binary-tree/
    def bottom_up_state_checker(self, binary_tree):
        return_type = self.ReturnType()

        # base case
        if not binary_tree:
            return_type.perfect = True
            return_type.complete = True
            return_type.size = 0
            return_type.root_node = None
            return return_type

        # recursively call on left and right subtree
        left_return_type = self.bottom_up_state_checker(binary_tree.left)
        right_return_type = self.bottom_up_state_checker(binary_tree.right)

        # if left subtree is perfect and right is complete or perfect and height is the same then root is complete or
        # perfect and size is size of left + right subtree + 1
        if left_return_type.perfect and right_return_type.complete and left_return_type.size == right_return_type.size:
            return_type.perfect = right_return_type.perfect
            return_type.complete = True
            return_type.size = left_return_type.size + right_return_type.size + 1
            return_type.root_node = binary_tree
            return return_type

        # if left subtree is complete and right is perfect but left is taller than right by 1 then root is complete
        if left_return_type.complete and right_return_type.perfect and left_return_type.size == right_return_type.size + 1:
            return_type.perfect = False
            return_type.complete = True
            return_type.size = left_return_type.size + right_return_type.size + 1
            return_type.root_node = binary_tree
            return return_type

        # otherwise from root it is not a complete tree
        return_type.perfect = False
        return_type.complete = False
        return_type.size = max(left_return_type.size, right_return_type.size)
        if left_return_type.size > right_return_type.size:
            return_type.root_node = left_return_type.root_node
        else:
            return_type.root_node = right_return_type.root_node
        return return_type
