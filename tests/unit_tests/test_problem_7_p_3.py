import pytest
from vlad.problem_7_p_3_vlad import Problem7P3Vlad
from protocol.problem_7_p_3 import LinkedList


class TestProblem7P3(object):
    def instantiate_solution(self):
        return Problem7P3Vlad()

    # list_a_looped is list_a with the looped elements added one more time
    @pytest.mark.parametrize("list_a, loop_idx, list_a_looped", [
        ([1, 2, 3, 4, 5], 3, [1, 2, 3, 4, 5, 3, 4, 5]),
        ([1, 2, 3], 3, [1, 2, 3, 3]),
        ([1, 2, 3], 1, [1, 2, 3, 1, 2, 3])
    ])
    def test_make_loop(self, list_a, loop_idx, list_a_looped):
        llist_a = LinkedList(list_a)
        llist_a.make_loop(loop_idx)
        llist_a_head = llist_a.head
        for elem in list_a_looped:
            assert llist_a_head.data == elem
            llist_a_head = llist_a_head.next

    @pytest.mark.parametrize("list_a, loop_idx", [
        ([11, 3, 5, 7, 2], 3),
        ([11, 3, 5, 7, 2], 1),
        ([11, 3, 5, 7, 2], 5),
        ([1], 1)
    ])
    def test_check_for_llist_cycle(self, list_a, loop_idx):
        llist_a = LinkedList(list_a)
        # this should always be none since the list was created with no loop originally
        assert self.instantiate_solution().check_for_llist_cycle(llist_a.head) == None
        llist_a.make_loop(loop_idx)   # created a loop in the list at loop_index
        assert self.instantiate_solution().check_for_llist_cycle(llist_a.head) == llist_a.get_node_at_idx(loop_idx)
