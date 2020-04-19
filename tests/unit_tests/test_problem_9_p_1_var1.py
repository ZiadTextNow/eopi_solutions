import pytest
from vlad.problem_9_p_1_var1_vlad import Problem9P1Var1Vlad
from protocol.problem_9_p_1 import BinaryTree


class TestProblem9P1Var1(object):
    def instantiate_solution(self):
        return Problem9P1Var1Vlad()

    @pytest.mark.parametrize("tree_data, largest_subtree", [
        ([2, 3, 1], 3),
        ([1, 3, 2], 2),
        ([1, 2, 3, 4], 1),
        ([5, 2, 3, 4, 1, 7, 6, 9, 10], 1),
        ([50, 30, 5, 20, 60, 55, 51, 70], 4)
    ])
    def test_largest_complete_subtree(self, tree_data, largest_subtree):
        test_tree = BinaryTree(tree_data)
        assert self.instantiate_solution().largest_complete_subtree(test_tree.get_root()) == largest_subtree
