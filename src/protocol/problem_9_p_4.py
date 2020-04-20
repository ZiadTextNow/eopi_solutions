from protocol.errors import EOPINotImplementedError


class Problem9P4(object):
    def lca_of_two_nodes(self, binary_tree, node_a, node_b):
        raise EOPINotImplementedError()


class BinaryParentTreeNode(object):
    def __init__(self, data=None, left=None, right=None, parent=None):
        self.data = data
        self.left = left
        self.right = right
        self.parent = parent


# I have defined this tree such that node.left.data < node.data <= node.right.data for convenience inserting and testing
# also wrote all the methods as iterative instead of recursive for practice :)
class BinaryParentTree(object):
    def __init__(self, tree_data=None):
        if tree_data:
            self._binary_tree = BinaryParentTreeNode(data=tree_data[0])
            for data in tree_data[1:]:
                self.insert(data)
        else:
            self._binary_tree = tree_data

    def get_root(self):
        return self._binary_tree if self._binary_tree else None

    # in order walk while comparing for data
    def get_node(self, data):
        root = self.get_root()
        left_done = False
        while True:
            # go as far left as possible
            if not left_done:  # this check is for the case when you got to this root from a left child
                while root.left:
                    root = root.left
            if root.data == data:  # keep checking for each step if the current node is the one with data
                return root
            left_done = True

            if root.right:
                root = root.right
                left_done = False
            # if we get here there are no left or right children we haven't seen and left_done is True
            elif root.parent:
                while root.parent and root.parent.right == root:
                    root = root.parent
                if not root.parent:
                    break
                root = root.parent
            else:
                break

    def insert(self, data):
        root = self.get_root()
        if not root:   # in the case that the binary tree has no data yet
            self._binary_tree = BinaryParentTreeNode(data)
            return
        while root:
            if data < root.data:
                if root.left:
                    root = root.left
                else:
                    root.left = BinaryParentTreeNode(data)
                    root.left.parent = root
                    break
            else:
                if root.right:
                    root = root.right
                else:
                    root.right = BinaryParentTreeNode(data)
                    root.right.parent = root
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

    def list_in_order_using_parent(self):
        root = self.get_root()
        list_in_order = []
        left_done = False
        while True:
            # go as far left as possible
            if not left_done:   # this check is for the case when you got to this root from a left child
                while root.left:
                    root = root.left
            list_in_order.append(root)
            left_done = True

            if root.right:
                root = root.right
                left_done = False
            # if we get here there are no left or right children we haven't seen and left_done is True
            elif root.parent:
                while root.parent and root.parent.right == root:
                    root = root.parent
                if not root.parent:
                    break
                root = root.parent
            else:
                break

