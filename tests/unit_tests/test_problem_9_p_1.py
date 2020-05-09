import pytest

from arshan.problem_9_p_1_arshan import Problem9P1Arshan
from vlad.problem_9_p_1_vlad import Problem9P1Vlad
from protocol.problem_9_p_1 import BinaryTree, BinaryTreeFactory


class TestProblem9P1(object):
    def instantiate_solution(self):
        return Problem9P1Arshan()
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

    @pytest.mark.parametrize("tree_dict, lnr_walk, nlr_walk, rnl_walk", [
        (
            {
                'v': 1,
                'l': {
                    'v': 2,
                },
                'r': {
                    'v': 3
                }
            },
            [2, 1, 3],
            [1, 2, 3],
            [3, 1, 2]
        ),
        (
            {
                'v': 1,
                'l': {
                    'v': 5
                },
                'r': {
                    'v': 2,
                    'r': {
                        'v': 3,
                        'r': {
                            'v': 12,
                            'r': {
                                'v': 15
                            }
                        }
                    }
                }
            },
            [5, 1, 2, 3, 12, 15],
            [1, 5, 2, 3, 12, 15],
            [15, 12, 3, 2, 1, 5]
        ),
        (
            {
                'v': 1,
                'l': {
                    'v': 5
                },
                'r': {
                    'v': 7,
                    'l': {
                        'v': 3,
                        'r': {
                            'v': 6,
                            'l': {
                                'v': 12
                            },
                            'r': {
                                'v': 14
                            }
                        }
                    }
                }
            },
            [5, 1, 3, 12, 6, 14, 7],
            [1, 5, 7, 3, 6, 12, 14],
            [7, 14, 6, 12, 3, 1, 5],
        )
    ])
    def test_construct_binary_tree_from_dict(self, tree_dict, lnr_walk, nlr_walk, rnl_walk):
        node = BinaryTreeFactory.construct_binary_tree_from_dict(tree_dict)
        assert BinaryTreeFactory.left_node_right_walk(node) == lnr_walk
        assert BinaryTreeFactory.node_left_right_walk(node) == nlr_walk
        assert BinaryTreeFactory.right_node_left_walk(node) == rnl_walk

    @pytest.mark.parametrize("tree_dict, height_balanced", [
        (
            {
                'v': 5,
                'l': {
                    'v': 2
                },
                'r': {
                    'v': 4
                }
            },
            True
        ),
        (
            {
                'v': 5,
                'l': {
                    'v': 2,
                    'l': {
                        'v': 5
                    }
                },
                'r': {
                    'v': 4
                }
            },
            True
        ),
        (
            {
                'v': 5,
                'l': {
                    'v': 2,
                    'l': {
                        'v': 5,
                        'r': {
                            'v': 2
                        }
                    }
                },
                'r': {
                    'v': 4
                }
            },
            False
        ),
        (
            {
                'v': 5,
                'l': {
                    'v': 2,
                    'l': {
                        'v': 5,
                        'r': {
                            'v': 2
                        }
                    }
                },
                'r': {
                    'v': 4,
                    'r': {
                        'v': 2
                    }
                }
            },
            False
        )
    ])
    def test_is_tree_balanced(self, tree_dict, height_balanced):
        node = BinaryTreeFactory.construct_binary_tree_from_dict(tree_dict)
        assert self.instantiate_solution().height_balanced(node) is height_balanced

