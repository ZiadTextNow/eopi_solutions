import pytest

from arshan.problem_8_p_1_arshan import Problem8P1Arshan
from vlad.problem_8_p_1_vlad import Problem8P1Vlad
from ziad.problem_8_p_1_ziad import Problem8P1Ziad


class TestProblem8P1(object):
    def instantiate_solution(self):
        return Problem8P1Arshan()
        return Problem8P1Vlad()
        # return Problem8P1Ziad()

    @pytest.mark.parametrize("push_vals, expected_stack", [
        ([1, 2, 3], [1, 2, 3]),
        ([1], [1]),
    ])
    def test_push(self, push_vals, expected_stack):
        stack = self.instantiate_solution().StackWithMax()
        for val in push_vals:
            stack.push(val)
        """
        I don't like that this assumes stack.pop() works but if I accessed elements by indices than I would have to
        get their .val attribute which is not a generic case and specific to my solution only
        """
        #while stack.stack:
        while not stack.is_empty():
            assert stack.pop() == expected_stack.pop()

    @pytest.mark.parametrize("stack_vals, pop_count, expected_stack", [
        ([1, 2, 3], 2, [1]),
        ([1, 2, 3], 1, [1, 2]),
    ])
    def test_pop(self, stack_vals, pop_count, expected_stack):
        stack = self.instantiate_solution().StackWithMax(stack_vals)
        for _ in range(pop_count):
            stack.pop()

        #while stack.stack:
        while not stack.is_empty():
            assert stack.pop() == expected_stack.pop()

    @pytest.mark.parametrize("stack_vals, pop_count", [
        ([1, 2, 3], 4),
        ([], 2),
    ])
    def test_pop_when_empty(self, stack_vals, pop_count):
        stack = self.instantiate_solution().StackWithMax(stack_vals)
        with pytest.raises(IndexError):
            for _ in range(pop_count):
                stack.pop()

    @pytest.mark.parametrize("stack_vals, max_val", [
        ([1, 2, 3], 3),
        ([1, 3, 2], 3),
        ([4, 1, 2], 4),
    ])
    def test_max(self, stack_vals, max_val):
        stack = self.instantiate_solution().StackWithMax(stack_vals)
        assert stack.max() == max_val

    @pytest.mark.parametrize("stack_vals", [
        [],
    ])
    def test_max_when_empty(self, stack_vals):
        stack = self.instantiate_solution().StackWithMax(stack_vals)
        with pytest.raises(IndexError):
            stack.max()

    @pytest.mark.parametrize("stack_vals, push_vals, max_val", [
        ([1, 2, 3], [1], 3),
        ([1, 3, 2], [4], 4),
        ([], [4], 4),
        ([], [4, 5, 6, 5], 6),
    ])
    def test_max_with_push(self, stack_vals, push_vals, max_val):
        stack = self.instantiate_solution().StackWithMax(stack_vals)
        for val in push_vals:
            stack.push(val)
        assert stack.max() == max_val

    @pytest.mark.parametrize("stack_vals, pop_count, max_val", [
        ([1, 2, 3], 1, 2),
        ([1, 3, 2], 1, 3),
        ([1, 2, 3, 4], 3, 1),
    ])
    def test_max_with_pop(self, stack_vals, pop_count, max_val):
        stack = self.instantiate_solution().StackWithMax(stack_vals)
        for _ in range(pop_count):
            stack.pop()
        assert stack.max() == max_val
