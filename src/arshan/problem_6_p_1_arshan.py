class Problem6P1Arshan(object):
    def str_to_int(self, str_of_int):
        lookup = {
            '-': -1, '0': 0, '1': 1, '2': 2,
            '3': 3, '4': 4, '5': 5, '6': 6,
            '7': 7, '8': 8, '9': 9
        }
        tens = 1
        r_val = 0
        for c in reversed(str_of_int):
            digit = lookup[c]
            if digit < 0:
                return -r_val
            r_val += digit * tens
            tens *= 10
        return r_val

    def int_to_str(self, int_of_str):
        if int_of_str == 0:
            return '0'
        lookup = {1: '1', 2: '2', 3: '3', 4: '4', 5: '5',
                  6: '6', 7: '7', 8: '8', 9: '9', 0: '0'}
        r_val = ""
        number = int_of_str
        if int_of_str <= 0:
            number *= -1
        while number:
            r_val += lookup[number % 10]
            number //= 10
        if int_of_str >= 0:
            return f"{self._reverse(r_val)}"
        return f"-{self._reverse(r_val)}"

    def _reverse(self, s):
        ret = ""
        for c in s:
            ret = c + ret
        return ret
