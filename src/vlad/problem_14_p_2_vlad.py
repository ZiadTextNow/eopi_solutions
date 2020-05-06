from protocol.problem_14_p_2 import Problem14P2

"""
THINGS TO NOTE ABOUT THIS PROBLEM

"""


class Problem14P2Vlad(Problem14P2):
    def first_key_greater(self, root, value):
        return self.walk_down_tree(root, value)

    def walk_down_tree(self, root, value):
        key_greater = None
        while root:
            if root.val > value:
                key_greater = root.val
                root = root.left
            else:
                root = root.right
        return key_greater
