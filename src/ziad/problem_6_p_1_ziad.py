from protocol.problem_6_p_1 import Problem6P1
import functools

'''    Interconvert Strings and Integers
 Notes: 
      1. code needs to be able to handle negative Integers
      2. code needs to be able to take either an integer or a string and return the other
'''


class Problem6P1Ziad(Problem6P1):
    def str_to_int(self, str_of_int):
        return self.more_elegant_str_to_int(str_of_int)

    def int_to_str(self, int_of_str):
        return self.naive_int_to_str(int_of_str)

    # Brute force approach:
    # Allocate a new string
    # time: O(n^2). O(n) for the while loop and O(n) because each time we append a new char to the string, we have to traverse it
    # space: O(n) because we are allocating memory for a new string/integer
    # -> if it's an integer, pop each digit by mod'ing with 10, append to new string and then return the reversed string
    def naive_int_to_str(self, int_of_str):
        integer = abs(int_of_str)
        output_string = ""

        if integer == 0:
            return "0"

        while True:
            if integer == 0:
                break

            popped_digit = integer % 10
            output_string += str(popped_digit)
            integer //= 10

        output_string = output_string[::-1]
        return output_string if int_of_str >= 0 else "-" + output_string

    # If it's a string, iterate over it in reversed order, while maintaining a counter.
    # For every digit, multiply that digit by 10^(counter),
    # e.g. "123" -> 3 * 10^0 + 2 * 10^1 + 1 * 10^2
    def more_elegant_str_to_int(self, str_of_int):
        int_so_far = 0
        tens_counter = 0

        for char in reversed(str_of_int):
            if char == "-":
                continue

            # brute force
            # int_so_far += int(char) * 10**tensCounter

            # more elegant
            int_so_far = int_so_far * 10 + int(char)

            tens_counter += 1

        return -int_so_far if str_of_int[0] == "-" else int_so_far

    # Using a higher-order function...
    def str_to_int_using_reduce(self, str_of_int):
        absolute_int = functools.reduce(
            lambda sum_so_far, char: sum_so_far * 10 + str.digits.index(char))

        return -1 * absolute_int if str_of_int[0] == "-" else absolute_int