import pytest

from arshan.problem_7_p_1_arshan import Problem7P1Arshan
from vlad.problem_7_p_1_vlad import Problem7P1Vlad
from protocol.problem_7_p_1 import LinkedList

"""
The testing for the LinkedList methods needs a better naming convention or some way to know that we are testing from
functions from protocol directory and from which class even. Not sure what the best way to do this is. For now I kept
this for this test and other problems to come :(
"""


class TestProblem7P1(object):
    def instantiate_solution(self):
        return Problem7P1Arshan()
        return Problem7P1Vlad()

    @pytest.mark.parametrize("list_a", [
        [1, 2, 3],
        [0, 5, 10, 100],
        [-1, 6, -6, 1],
    ])
    def test_create_linked_list(self, list_a):
        list = LinkedList(list_a)
        assert list.to_list() == list_a

    def _node_to_normal_list(self, node):
        l = []
        while(node):
            l.append(node.data)
            node = node.next
        return l

    @pytest.mark.parametrize("list_a, list_b, list_expected", [
        ([1, 3, 5], [2, 4], [1, 2, 3, 4, 5]),
        ([2, 5, 7], [3, 11], [2, 3, 5, 7, 11]),
        ([1, 2, 3], [], [1, 2, 3]),
        ([], [1, 2, 3], [1, 2, 3]),
        ([1, 2, 3], [4, 5, 6], [1, 2, 3, 4, 5, 6]),
    ])
    def test_merge_two_sorted_llists(self, list_a, list_b, list_expected):
        llist_a = LinkedList(list_a)
        llist_b = LinkedList(list_b)
        merged = self.instantiate_solution().merge_two_sorted_llists(llist_a.head, llist_b.head)
        assert self._node_to_normal_list(merged) == list_expected
