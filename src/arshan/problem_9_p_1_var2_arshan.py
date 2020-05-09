from protocol.problem_9_p_1_var2 import Problem9P1Var2


class Problem9P1Var2Arshan(Problem9P1Var2):
    def __init__(self):
        self.not_k_nodes = []

    def not_k_balanced_tree(self, binary_tree, k):
        self.not_k_nodes = []
        def check_size(node):
            if not node:
                return 0, True
            l, lb = check_size(node.left)
            r, rb = check_size(node.right)
            if abs(l - r) > k:
                if lb and rb:
                    self.not_k_nodes.append(node)
                return l + r + 1, False
            else:
                return l + r + 1, True
        check_size(binary_tree)
        return self.not_k_nodes[0].data
