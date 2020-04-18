import pytest
from vlad.problem_7_p_2_vlad import Problem7P2Vlad
from protocol.problem_7_p_1 import LinkedList


class TestProblem7P2(object):
    def instantiate_solution(self):
        return Problem7P2Vlad()

    @pytest.mark.parametrize("list_a, s, f, list_expected", [
        ([11, 3, 5, 7, 2], 2, 4, [11, 7, 5, 3, 2]),
        ([11, 3, 5, 7, 2], 1, 4, [7, 5, 3, 11, 2]),
        ([11, 3, 5, 7, 2], 1, 5, [2, 7, 5, 3, 11]),
    ])
    def test_merge_two_sorted_llists(self, list_a, s, f, list_expected):
        llist_a = LinkedList(list_a)
        llist_a_head = self.instantiate_solution().reverse_sublist(llist_a.head, s, f)
        for elem in list_expected:
            assert llist_a_head.data == elem
            llist_a_head = llist_a_head.next


