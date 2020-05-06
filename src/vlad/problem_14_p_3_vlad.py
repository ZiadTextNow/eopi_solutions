from protocol.problem_14_p_3 import Problem14P3

"""
THINGS TO NOTE ABOUT THIS PROBLEM

"""


class Problem14P3Vlad(Problem14P3):
    def k_largest_elements(self, root, k):
        # return self.reverse_in_order_iterative(root, k)
        return self.reverse_in_order_recursive(root, k)

    def reverse_in_order_iterative(self, root, k):
        node_stack = []
        result_nodes = []
        while len(result_nodes) < k:
            if root:
                node_stack.append(root)
                root = root.right
            elif node_stack:
                node = node_stack.pop()
                result_nodes.append(node.val)
                root = node.left
        return result_nodes

    def reverse_in_order_recursive(self, root, k):
        result_nodes = []
        def inner_func(root):
            if root:
                inner_func(root.right)
                if len(result_nodes) < k:
                    result_nodes.append(root.val)
                    inner_func(root.left)
        inner_func(root)
        return result_nodes
