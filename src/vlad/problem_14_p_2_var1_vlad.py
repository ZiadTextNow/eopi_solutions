from protocol.problem_14_p_2_var1 import Problem14P2Var1

"""
THINGS TO NOTE ABOUT THIS PROBLEM

"""


class Problem14P2Var1Vlad(Problem14P2Var1):
    def first_node_equal(self, root, value):
        return self.walk_down_tree(root, value)

    def walk_down_tree(self, root, value):
        node_equal = None
        while root:
            if root.val < value:
                root = root.right
            elif root.val == value:
                node_equal = root
                root = root.left
            else:
                root = root.left
        return node_equal
