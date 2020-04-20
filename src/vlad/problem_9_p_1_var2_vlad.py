from protocol.problem_9_p_1_var2 import Problem9P1Var2
import math

"""
THINGS TO NOTE ABOUT THIS PROBLEM
"""


class Problem9P1Var2Vlad(Problem9P1Var2):
    def not_k_balanced_tree(self, binary_tree, k):
        return self.bottom_up_state_checker(binary_tree, k).root_node.data

    class ReturnType(object):
        def __init__(self, balanced=None, size=0, root_node=None):
            self.balanced = balanced
            self.size = size
            self.root_node = root_node

    # using very similar idea to problem 9.1var2
    def bottom_up_state_checker(self, binary_tree, k):
        return_type = self.ReturnType()

        # base case
        if not binary_tree:
            return_type.balanced = True
            return_type.size = 0
            return_type.root_node = None
            return return_type

        # recursively call on left and right subtree
        left_return_type = self.bottom_up_state_checker(binary_tree.left, k)
        right_return_type = self.bottom_up_state_checker(binary_tree.right, k)

        # if left subtree is not k balanced then set current return types root_node to the left subtrees root node
        # do the same for right subtree only if left is balanced. This method a has a bias for left subtree if both are
        # unbalanced
        if not left_return_type.balanced:
            return_type.balanced = False
            return_type.root_node = left_return_type.root_node
            return return_type
        elif not right_return_type.balanced:
            return_type.balanced = False
            return_type.root_node = right_return_type.root_node
            return return_type

        # if the magnitude of size of left subtree - size of right subtree is > 3 then the tree at the current root is
        # not k balanced
        if abs(left_return_type.size - right_return_type.size) > k:
            return_type.balanced = False
            return_type.root_node = binary_tree
            return return_type

        # if we get here then both subtrees are balanced and the current root is balanced
        return_type.balanced = True
        return_type.size = left_return_type.size + right_return_type.size + 1
        return return_type
