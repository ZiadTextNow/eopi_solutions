from protocol.errors import EOPINotImplementedError


class Problem14P1(object):
    def is_binary_search_tree(self, root):
        raise EOPINotImplementedError()


class TreeNode(object):
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    @staticmethod
    def create_tree(vals_list):
        """
        We implement this as a complete binary tree for ease of testing
                     0
                1         2
             3    4    5     6
           7  8 9 10 11 12 13 14
        we use the fact that in a complete binary tree a node i's children are at i*2 + 1 and i*2 + 2 in the vals_list
        :param vals_list: all the elements that are to be placed in the complete binary tree
        :return: the root node of the complete binary tree
        """
        if not vals_list:  # if there are no values
            return None
        # replace each list element with a TreeNode object
        for i, val in enumerate(vals_list):
            vals_list[i] = TreeNode(val)
        cur_node_idx = 0
        while True:
            cur_node = vals_list[cur_node_idx]
            left_child_idx = cur_node_idx * 2 + 1
            right_child_idx = cur_node_idx * 2 + 2
            if left_child_idx >= len(vals_list):
                break
            cur_node.left = vals_list[left_child_idx]
            if right_child_idx >= len(vals_list):
                break
            cur_node.right = vals_list[right_child_idx]
            cur_node_idx += 1
        return vals_list[0]   # this is root of the tree

    @staticmethod
    def get_in_order_list(root):
        in_order_list = []
        node_stack = []
        while True:
            if root:
                node_stack.append(root)
                root = root.left
            elif node_stack:
                node = node_stack.pop()
                in_order_list.append(node.val)
                root = node.right
            else:
                break
        return in_order_list





