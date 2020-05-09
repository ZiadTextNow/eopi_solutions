from protocol.problem_9_p_1 import Problem9P1


class Problem9P1Var1Arshan(Problem9P1):
    def __init__(self):
        self.max = 0
        self.size = 0

    def largest_complete_subtree(self, node):
        return self.largest_complete_subtree_size(node)

    def largest_complete_subtree_height(self, node):
        self.max = 0
        def height_if_complete(n):
            if not n:
                return 0
            l = height_if_complete(n.left)
            r = height_if_complete(n.right)
            self.max = max(self.max, l, r)
            return max(l, r) + 1 if abs(l - r) < 2 else 0
        return height_if_complete(node) or self.max

    def largest_complete_subtree_size(self, node):
        self.size = 0
        def size_if_complete(n):
            if not n:
                return 0
            l = size_if_complete(n.left)
            r = size_if_complete(n.right)
            self.size = max(self.size, l, r)
            return l + r + 1 if abs(l - r) < 2 else 0
        return size_if_complete(node) or self.size

