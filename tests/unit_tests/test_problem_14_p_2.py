import pytest
from protocol.problem_14_p_1 import TreeNode
from vlad.problem_14_p_2_vlad import Problem14P2Vlad


class TestProblem14P2(object):
    def instantiate_solution(self):
        return Problem14P2Vlad()

    @pytest.mark.parametrize("vals_list, value, key_greater", [
        ([4, 2, 6, 1, 3, 5, 7], 1, 2),
        ([4, 2, 6, 1, 3, 5, 7], 2, 3),
        ([4, 2, 6, 1, 3, 5, 7], 3, 4),
        ([4, 2, 6, 1, 3, 5, 7], 4, 5),
        ([4, 2, 6, 1, 3, 5, 7], 5, 6),
        ([4, 2, 6, 1, 3, 5, 7], 6, 7),
        ([19, 7, 43, 3, 11, 23, 47, 2, 5, 13, 17, 21, 29, 45, 53], 23, 29)
    ])
    def test_first_key_greater(self, vals_list, value, key_greater):
        tree_root = TreeNode.create_tree(vals_list)
        assert self.instantiate_solution().first_key_greater(tree_root, value) == key_greater
