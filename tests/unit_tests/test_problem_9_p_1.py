import pytest
from vlad.problem_9_p_1_vlad import Problem9P1Vlad
from protocol.problem_9_p_1 import BinaryTree


class TestProblem9P1(object):
    def instantiate_solution(self):
        return Problem9P1Vlad()

    @pytest.mark.parametrize("insert_data, expected_in_order_walk", [
        ([2, 3, 1], [1, 2, 3]),
        ([1], [1]),
        ([1, 2, 3], [1, 2, 3]),
    ])
    def test_insert(self, insert_data, expected_in_order_walk):
        test_tree = BinaryTree()
        for data in insert_data:
            test_tree.insert(data)
        assert test_tree.list_in_order() == expected_in_order_walk

    @pytest.mark.parametrize("tree_data, expected_in_order_walk", [
        ([2, 3, 1], [1, 2, 3]),
        ([1], [1]),
        ([1, 2, 3], [1, 2, 3]),
    ])
    def test_init(self, tree_data, expected_in_order_walk):
        test_tree = BinaryTree(tree_data)
        assert test_tree.list_in_order() == expected_in_order_walk

    @pytest.mark.parametrize("tree_data, root", [
        ([2, 3, 1], 2),
        ([1], 1),
        ([1, 2, 3], 1),
    ])
    def test_get_root(self, tree_data, root):
        test_tree = BinaryTree(tree_data)
        assert test_tree.get_root().data == root

    @pytest.mark.parametrize("tree_data, is_height_balanced", [
        ([2, 3, 1], True),
        ([1, 3, 2], False),
        ([1, 2, 3, 4], False),
        ([5, 2, 3, 4, 1, 7, 6, 9, 10], True),
    ])
    def test_height_balanced(self, tree_data, is_height_balanced):
        test_tree = BinaryTree(tree_data)
        assert self.instantiate_solution().height_balanced(test_tree.get_root()) == is_height_balanced
