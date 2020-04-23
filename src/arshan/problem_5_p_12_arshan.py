import random

from protocol.problem_5_p_12 import Problem5P12


class Problem5P12Arshan(Problem5P12):
    def random_sampling(self, distinct_elem_list, size):
        A = distinct_elem_list
        o = []
        while len(o) < size:
            r = random.randint(0, len(A) - 1)
            o.append(distinct_elem_list.pop(r))
        return o
