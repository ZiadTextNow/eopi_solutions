from protocol.problem_9_p_4 import Problem9P4

"""
THINGS TO NOTE ABOUT THIS PROBLEM

in their solution they seem to believe that if both nodes are the same then the LCA is the node they both are. I think
it should actually be their parent since they are not ancestors of them selves...
"""


class Problem9P4Vlad(Problem9P4):
    def lca_of_two_nodes(self, binary_tree, node_a, node_b):
        return self.same_height_climb(binary_tree, node_a, node_b)

    # get both nodes to the same height then just climb simultaneously from there until both are equal
    def same_height_climb(self, binary_tree, node_a, node_b):
        if node_a == node_b:
            return node_a.parent

        node_a_height = self.node_height(binary_tree, node_a)
        node_b_height = self.node_height(binary_tree, node_b)

        # this get the deeper node to the same height
        while node_a_height > node_b_height:
            node_a = node_a.parent
            node_a_height -= 1
        while node_b_height > node_a_height:
            node_b = node_b.parent
            node_b_height -= 1

        if node_a == node_b:   # this is if the same height is the same node so the parent would be the LCA
            return node_a.parent
        while node_a != node_b:
            node_a = node_a.parent
            node_b = node_b.parent
        return node_a

    class ReturnType(object):
        def __init__(self, found=None, height=0):
            self.found = found
            self.height = height

    # I clearly didn't realize that there was a parent field...
    def node_height(self, binary_tree, node_a):
        def inner_func(binary_tree, node_a, height):
            return_type = self.ReturnType()

            if not binary_tree:
                return_type.found, return_type.height = False, height
                return return_type
            if binary_tree == node_a:
                return_type.found, return_type.height = True, height
                return return_type

            left_return_type = inner_func(binary_tree.left, node_a, height + 1)
            right_return_type = inner_func(binary_tree.right, node_a, height + 1)

            if not left_return_type.found and not right_return_type.found:
                return_type.found, return_type.height = False, height
            elif left_return_type.found:
                return_type.found, return_type.height = True, left_return_type.height
            elif right_return_type.found:
                return_type.found, return_type.height = True, right_return_type.height
            return return_type

        return inner_func(binary_tree, node_a, 0).height
