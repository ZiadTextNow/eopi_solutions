from protocol.problem_14_p_1 import Problem14P1
import bintrees

"""
THINGS TO NOTE ABOUT THIS PROBLEM

"""


class Problem14P1Vlad(Problem14P1):
    def is_binary_search_tree(self, root):
        return self.recrusive_depth_first(root)

    def recrusive_depth_first(self, root):
        if not root:
            return True
        if root.left and root.left.val > root.val:
            return False
        if root.right and root.right.val < root.val:
            return False

        return self.recrusive_depth_first(root.left) and self.recrusive_depth_first(root.right)
