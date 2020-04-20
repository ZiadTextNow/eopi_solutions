import pytest
from vlad.problem_9_p_1_var2_vlad import Problem9P1Var2Vlad
from protocol.problem_9_p_1 import BinaryTree


class TestProblem9P1Var2(object):
    def instantiate_solution(self):
        return Problem9P1Var2Vlad()

    @pytest.mark.parametrize("tree_data, k, not_k_balanced_node_data", [
        ([1, 3, 2], 1, 1),
        ([1, 2, 3, 4], 1, 2),
        ([5, 2, 3, 4, 1], 3, 5),
        ([5, 2, 3, 4, 1, 6, 7, 9, 8, 10, 12, 11, 14, 13], 3, 10),
    ])
    def test_not_k_balanced_tree(self, tree_data, k, not_k_balanced_node_data):
        test_tree = BinaryTree(tree_data)
        assert self.instantiate_solution().not_k_balanced_tree(test_tree.get_root(), k) == not_k_balanced_node_data
