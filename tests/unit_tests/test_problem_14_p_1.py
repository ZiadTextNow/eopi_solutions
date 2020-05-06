import pytest
from protocol.problem_14_p_1 import TreeNode
from vlad.problem_14_p_1_vlad import Problem14P1Vlad


class TestProblem14P1(object):
    def instantiate_solution(self):
        return Problem14P1Vlad()

    @pytest.mark.parametrize("vals_list, in_order_list", [
        ([1, 2, 3, 4, 5, 6, 7], [4, 2, 5, 1, 6, 3, 7]),
        ([1, 2, 3, 4, 5, 6], [4, 2, 5, 1, 6, 3]),
        ([1, 2, 3, 4, 5], [4, 2, 5, 1, 3]),
        ([1, 2, 3, 4], [4, 2, 1, 3]),
        ([1, 2, 3], [2, 1, 3]),
        ([1, 2], [2, 1]),
        ([1], [1]),
        ([], []),
    ])
    def test_tree_node_create_tree(self, vals_list, in_order_list):
        tree_root = TreeNode.create_tree(vals_list)
        assert TreeNode.get_in_order_list(tree_root) == in_order_list

    @pytest.mark.parametrize("vals_list, is_bst", [
        ([1, 2, 3, 4, 5, 6, 7], False),
        ([4, 2, 6, 1, 3, 5, 7], True),
    ])
    def test_is_binary_search_tree(self, vals_list, is_bst):
        tree_root = TreeNode.create_tree(vals_list)
        assert self.instantiate_solution().is_binary_search_tree(tree_root) == is_bst
