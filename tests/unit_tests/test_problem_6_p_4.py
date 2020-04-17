import pytest
from vlad.problem_6_p_4_vlad import Problem6P4Vlad


class TestProblem6P4(object):
    def instantiate_solution(self):
        return Problem6P4Vlad()

    @pytest.mark.parametrize("str_list, size, expected_str_list, final_size", [
        (['a', 'c', 'd', 'b', 'b', 'c', 'a'], 7, ['d', 'd', 'c', 'd', 'c', 'd', 'd'], 7),
        (['a', 'b', 'a', 'c', '-'], 4, ['d', 'd', 'd', 'd', 'c'], 5),
        (['a', 'b', 'b', 'c'], 4, ['d', 'd', 'c', '-'], 3),
        (['a'] * 3 + ['-'] * 3, 3, ['d'] * 6, 6),
        (['b'] * 3, 3, ['-'] * 3, 0)
    ])
    def test_int_to_str(self, str_list, size, expected_str_list, final_size):
        self.instantiate_solution().replace_and_remove(str_list, size)
        assert str_list[0:final_size] == expected_str_list[0:final_size]
