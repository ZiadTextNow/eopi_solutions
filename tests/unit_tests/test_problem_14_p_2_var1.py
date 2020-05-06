import pytest
from protocol.problem_14_p_1 import TreeNode
from vlad.problem_14_p_2_var1_vlad import Problem14P2Var1Vlad


class TestProblem14P2Var1(object):
    def instantiate_solution(self):
        return Problem14P2Var1Vlad()

    """
    Alright I know this is a pretty dirty way to test for the correct node but I'm gonna do it anyway!
    We use the fact that the vals_list actually becomes a list of all the nodes in the bst when the TreeNode.create_tree
    is called. And since it's a complete tree we know exactly which index in the list each node is. So for the test we 
    use the list index to retrieve the right node :) 
    """
    @pytest.mark.parametrize("vals_list, value, node_idx", [
        ([4, 2, 6, 1, 3, 5, 7], 1, 3),
        ([4, 2, 6, 1, 3, 5, 7], 2, 1),
        ([4, 2, 6, 1, 3, 5, 7], 3, 4),
        ([4, 2, 6, 1, 3, 5, 7], 4, 0),
        ([4, 2, 6, 1, 3, 5, 7], 5, 5),
        ([4, 2, 6, 1, 3, 5, 7], 6, 2),
        ([4, 2, 6, 1, 3, 5, 7], 7, 6),
        ([108, 108, 285, -10, 108, 243, 285], 108, 1),
        ([108, 108, 285, -10, 108, 243, 285], 285, 2),
        ([108, 108, 285, -10, 108, 243, 285], 143, None),
    ])
    def test_first_node_equal(self, vals_list, value, node_idx):
        tree_root = TreeNode.create_tree(vals_list)
        node_equal = vals_list[node_idx] if node_idx is not None else None
        assert self.instantiate_solution().first_node_equal(tree_root, value) == node_equal
