import pytest
from vlad.problem_8_p_6_vlad import Problem8P6Vlad
from protocol.problem_9_p_1 import BinaryTree


class TestProblem8P6(object):
    def instantiate_solution(self):
        return Problem8P6Vlad()

    @pytest.mark.parametrize("tree_data, bfs_list", [
        ([2, 3, 1], [[2], [1, 3]]),
        ([1, 3, 2], [[1], [3], [2]]),
        ([1, 2, 3, 4], [[1], [2], [3], [4]]),
        ([5, 2, 3, 4, 1, 7, 6, 9, 10], [[5], [2, 7], [1, 3, 6, 9], [4, 10]]),
    ])
    def test_breadth_first_search(self, tree_data, bfs_list):
        test_tree = BinaryTree(tree_data)
        assert self.instantiate_solution().breadth_first_search(test_tree.get_root()) == bfs_list
