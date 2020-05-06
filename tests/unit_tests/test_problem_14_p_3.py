import pytest
from protocol.problem_14_p_1 import TreeNode
from vlad.problem_14_p_3_vlad import Problem14P3Vlad


class TestProblem14P3(object):
    def instantiate_solution(self):
        return Problem14P3Vlad()

    @pytest.mark.parametrize("vals_list, k, k_largest", [
        ([4, 2, 6, 1, 3, 5, 7], 1, [7]),
        ([4, 2, 6, 1, 3, 5, 7], 2, [7, 6]),
        ([4, 2, 6, 1, 3, 5, 7], 3, [7, 6, 5]),
        ([4, 2, 6, 1, 3, 5, 7], 4, [7, 6, 5, 4]),
        ([4, 2, 6, 1, 3, 5, 7], 5, [7, 6, 5, 4, 3]),
        ([4, 2, 6, 1, 3, 5, 7], 6, [7, 6, 5, 4, 3, 2]),
        ([4, 2, 6, 1, 3, 5, 7], 7, [7, 6, 5, 4, 3, 2, 1]),
        ([19, 7, 43, 3, 11, 23, 47, 2, 5, 13, 17, 21, 29, 43, 53], 3, [53, 47, 43])
    ])
    def test_k_largest_elements(self, vals_list, k, k_largest):
        tree_root = TreeNode.create_tree(vals_list)
        assert self.instantiate_solution().k_largest_elements(tree_root, k) == k_largest
