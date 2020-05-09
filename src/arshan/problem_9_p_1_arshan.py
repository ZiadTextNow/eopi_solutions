class Problem9P1Arshan(object):
    def height_balanced(self, node):
        #return self.short_circuit_solution(node)
        return self.naive_solution(node)

    """
    1. get height
    2. get difference 
    3. return
    """
    def naive_solution(self, node):
        def get_height(node, height=0):
            if not node:
                return height
            height += 1
            return max(
                get_height(node.left, height),
                get_height(node.right, height)
            )

        def check_height(node):
            if not node:
                return True
            if not check_height(node.left):
                return False
            if not check_height(node.right):
                return False
            h_left = get_height(node.left)
            h_right = get_height(node.right)
            return abs(
                h_left - h_right
            ) < 2
        return check_height(node)


    """
    idea: if a subtree ain't balanced then the whole thing ain't balanced.
    short-circuit to a NAH if the subtree ain't balanced.
    I wanna do a traversal and keep track of the heights of each subtree.
    looks like left, right, node is the right kind of traversal
    """
    def short_circuit_solution(self, node):
        def _short_circuit(node):
            if not node:
                return True, 0
            height_left, height_right = 0, 0
            if node.left:
                balanced, height_left = _short_circuit(node.left)
                if not balanced:
                    return False, 0
            if node.right:
                balanced, height_right = _short_circuit(node.right)
                if not balanced:
                    return False, 0
            if abs(height_left - height_right) > 1:
                return False, 0
            return True, max(height_right, height_left) + 1
        return _short_circuit(node)[0]


