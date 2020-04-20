import pytest
from vlad.problem_9_p_4_vlad import Problem9P4Vlad
from protocol.problem_9_p_4 import BinaryParentTree


class TestProblem9P4(object):
    def instantiate_solution(self):
        return Problem9P4Vlad()

    @pytest.mark.parametrize("insert_data, expected_in_order_walk", [
        ([2, 3, 1], [1, 2, 3]),
        ([1], [1]),
        ([1, 2, 3], [1, 2, 3]),
    ])
    def test_insert(self, insert_data, expected_in_order_walk):
        test_tree = BinaryParentTree()
        for data in insert_data:
            test_tree.insert(data)
        assert test_tree.list_in_order() == expected_in_order_walk

    @pytest.mark.parametrize("tree_data, expected_in_order_walk", [
        ([2, 3, 1], [1, 2, 3]),
        ([1], [1]),
        ([1, 2, 3], [1, 2, 3]),
    ])
    def test_init(self, tree_data, expected_in_order_walk):
        test_tree = BinaryParentTree(tree_data)
        assert test_tree.list_in_order() == expected_in_order_walk

    @pytest.mark.parametrize("tree_data, root", [
        ([2, 3, 1], 2),
        ([1], 1),
        ([1, 2, 3], 1),
    ])
    def test_get_root(self, tree_data, root):
        test_tree = BinaryParentTree(tree_data)
        assert test_tree.get_root().data == root

    @pytest.mark.parametrize("tree_data, node_a_data, node_b_data, lca_of_two_nodes_data", [
        ([2, 3, 1], 3, 1, 2),
        ([1, 3, 2], 3, 2, 1),
        ([1, 3, 2], 2, 3, 1),
        ([1, 2, 3, 4], 4, 3, 2),
        ([5, 2, 3, 4, 1, 7, 6, 9, 10], 4, 9, 5),
    ])
    def test_lca_of_two_nodes(self, tree_data, node_a_data, node_b_data, lca_of_two_nodes_data):
        test_tree = BinaryParentTree(tree_data)
        node_a = test_tree.get_node(node_a_data)
        node_b = test_tree.get_node(node_b_data)
        lca_of_two_nodes = test_tree.get_node(lca_of_two_nodes_data)
        assert self.instantiate_solution().lca_of_two_nodes(test_tree.get_root(), node_a, node_b) == lca_of_two_nodes
