from protocol.errors import EOPINotImplementedError


class Problem9P1(object):
    def height_balanced(self, binary_tree):
        raise EOPINotImplementedError()


class BinaryTreeFactory(object):
    """
    A helper class for constructing more, different kinds of binary tree,
    not necessarily sorted or balanced... This is used in more miscellaneous test cases.
    """

    """
    here, we can create a tree from a dict, each node in the dict has l, r, and v:
        l: left
        r: right
        v: value
    e.g: {v:1, l: None, r: None} is:
        1
    e.g: {
            v: 1,
            l: None
            r: {
                v: 1,
                l: None,
                r: None
            }
         } 
         is:
    1
      \ 
        1
    A more complex tree: 
    {
        v: 1,
        l: {
            v: 1,
            l: None,
            r: None
        },
        r: {
            v: 0,
            l: {
                v:1,
                l: None,
                r: None
            }
            r: {
                v: 0,
                l: {
                    v: 5, # we can ommit left and right, they're assumed to be None
                },
                r: {
                    v: 7,
                    r: {
                        v: 8,
                    }
                }
            }
        }
    }
    leads to: 
          1
        /    \ 
       1      0
             /  \ 
            1    0 
                / \ 
               5   7
                    \ 
                      8
    """
    @classmethod
    def construct_binary_tree_from_dict(cls, elements):
        if not elements or 'v' not in elements:
            return None
        root_node, left_node, right_node = BinaryTreeNode(data=elements['v']), None, None
        if 'l' in elements:
            left_node = cls.construct_binary_tree_from_dict(elements['l'])
        if 'r' in elements:
            right_node = cls.construct_binary_tree_from_dict(elements['r'])
        root_node.left = left_node
        root_node.right = right_node
        return root_node

    @classmethod
    def right_node_left_walk(cls, node):
        return cls.ordered_walk(node, 'rnl')

    @classmethod
    def node_left_right_walk(cls, node):
        return cls.ordered_walk(node, 'nlr')

    @classmethod
    def left_node_right_walk(cls, node):
        return cls.ordered_walk(node, 'lnr')

    @classmethod
    def ordered_walk(cls, node, order):
        def _ordered_recursive(node, out):
            order_lookup = {
                'l': lambda node, out: _ordered_recursive(node.left, out),
                'r': lambda node, out: _ordered_recursive(node.right, out),
                'n': lambda node, out: out.append(node.data),
            }
            if not node:
                return
            for c in order:
                order_lookup[c](node, out)
        out = []
        _ordered_recursive(node, out)
        return out


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
