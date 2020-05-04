import pytest
from vlad.problem_6_p_1_vlad import Problem6P1Vlad
# from ziad.problem_6_p_1_ziad import Problem6P1Ziad

class TestProblem6P1(object):
    def instantiate_solution(self):
        return Problem6P1Vlad()
        # return Problem6P1Ziad()

    @pytest.mark.parametrize("int_of_str, str_of_int", [
        (123, '123'),
        (0, '0'),
        (192837465, '192837465'),
        (-123, '-123'),
        (-192837465, '-192837465'),
    ])
    def test_int_to_str(self, int_of_str, str_of_int):
        assert self.instantiate_solution().int_to_str(int_of_str) == str_of_int

    @pytest.mark.parametrize("str_of_int, int_of_str", [
        ('123', 123),
        ('0', 0),
        ('192837465', 192837465),
        ('-123', -123),
        ('-0', 0),
        ('-192837465', -192837465),
    ])
    def test_str_to_int(self, str_of_int, int_of_str):
        assert self.instantiate_solution().str_to_int(str_of_int) == int_of_str
