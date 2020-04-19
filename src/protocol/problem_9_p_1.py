from protocol.errors import EOPINotImplementedError


class Problem9P1(object):
    def height_balanced(self, binary_tree):
        raise EOPINotImplementedError()


# copied from page 112 of the book
class BinaryTreeNode(object):
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


# I have defined this tree such that node.left.data < node.data <= node.right.data for convenience inserting and testing
# also wrote all the methods as iterative instead of recursive for practice :)
class BinaryTree(object):
    def __init__(self, tree_data=None):
        if tree_data:
            self._binary_tree = BinaryTreeNode(data=tree_data[0])
            for data in tree_data[1:]:
                self.insert(data)
        else:
            self._binary_tree = tree_data

    def get_root(self):
        return self._binary_tree if self._binary_tree else None

    def insert(self, data):
        root = self.get_root()
        if not root:   # in the case that the binary tree has no data yet
            self._binary_tree = BinaryTreeNode(data)
            return
        while root:
            if data < root.data:
                if root.left:
                    root = root.left
                else:
                    root.left = BinaryTreeNode(data)
                    break
            else:
                if root.right:
                    root = root.right
                else:
                    root.right = BinaryTreeNode(data)
                    break

    def list_in_order(self):
        root = self.get_root()
        list_in_order = []
        node_stack = []
        while True:
            if root:
                node_stack.append(root)
                root = root.left
            elif node_stack:
                root = node_stack.pop()
                list_in_order.append(root.data)
                root = root.right
            else:
                break
        return list_in_order
