import pytest

from arshan.problem_7_p_1_var1_arshan import Problem7P1Var1Arshan
from vlad.problem_7_p_1_var1_vlad import Problem7P1Var1Vlad
from protocol.problem_7_p_1_var1 import DoublyLinkedList


class TestProblem7P1Var1(object):
    def instantiate_solution(self):
        return Problem7P1Var1Arshan()
        return Problem7P1Var1Vlad()

    @pytest.mark.parametrize("list_a", [
        [1, 2, 3],
        [0, 5, 10, 100],
        [-1, 6, -6, 1],
    ])
    def test_create_linked_list(self, list_a):
        head = DoublyLinkedList(list_a).head
        for elem in list_a:
            assert head.data == elem
            head = head.next

    @pytest.mark.parametrize("list_a, list_b, list_expected", [
        ([1, 3, 5], [2, 4], [1, 2, 3, 4, 5]),
        ([2, 5, 7], [3, 11], [2, 3, 5, 7, 11]),
        ([1, 2, 3], [], [1, 2, 3]),
        ([], [1, 2, 3], [1, 2, 3]),
        ([1, 2, 3], [4, 5, 6], [1, 2, 3, 4, 5, 6]),
    ])
    def test_merge_two_sorted_llists(self, list_a, list_b, list_expected):
        dllist_a = DoublyLinkedList(list_a)
        dllist_b = DoublyLinkedList(list_b)
        dllist_actual_head = self.instantiate_solution().merge_two_sorted_dllists(dllist_a.head, dllist_b.head)
        for num, elem in enumerate(list_expected):
            assert dllist_actual_head.data == elem
            if num != len(list_expected) - 1:
                dllist_actual_head = dllist_actual_head.next
        for elem in reversed(list_expected):
            assert dllist_actual_head.data == elem
            dllist_actual_head = dllist_actual_head.previous


