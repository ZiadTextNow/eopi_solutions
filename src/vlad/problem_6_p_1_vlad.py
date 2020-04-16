from protocol.problem_6_p_1 import Problem6P1

"""
THINGS TO NOTE ABOUT THIS PROBLEM

ord(char) gives you the ASCII value
chr(int) gives you the char that represents the int according to the ASCII value
"""


class Problem6P1Vlad(Problem6P1):
    def str_to_int(self, str_of_int):
        return self.iterative_int_add(str_of_int)

    def int_to_str(self, int_of_str):
        # return self.iterative_str_append(int_of_str)
        return self.using_str_join(int_of_str)

    # pretty sure this is just as fast as the books solution not sure why one is preferred of other?
    def iterative_int_add(self, str_of_int):
        int_of_str = 0
        offset = -ord('0')
        for i in reversed(range(len(str_of_int))):
            if str_of_int[i] == '-':
                int_of_str *= -1
            else:
                int_of_char = ord(str_of_int[i]) + offset
                int_of_str += int_of_char * 10**(len(str_of_int) - i - 1)
        return int_of_str


    def iterative_str_append(self, int_of_str):
        if not int_of_str:   # if input is 0
            return chr(ord('0'))
        str_of_int = ''
        offset = ord('0')
        sign = ''
        if int_of_str < 0:
            sign = '-'
            int_of_str *= -1
        while int_of_str:
            lsd = int_of_str % 10   # lsd = least significant digit
            char_of_int = chr(lsd + offset)
            str_of_int += char_of_int
            int_of_str //= 10
        str_of_int += sign
        return str_of_int[::-1]

    def using_str_join(self, int_of_str):
        if not int_of_str:   # if input is 0
            return chr(ord('0'))
        str_of_int_list = []
        offset = ord('0')
        sign = ''
        if int_of_str < 0:
            sign = '-'
            int_of_str *= -1
        while int_of_str:
            lsd = int_of_str % 10  # lsd = least significant digit
            char_of_int = chr(lsd + offset)
            str_of_int_list.append(char_of_int)
            int_of_str //= 10
        str_of_int_list.append(sign)
        return ''.join(str_of_int_list)[::-1]
