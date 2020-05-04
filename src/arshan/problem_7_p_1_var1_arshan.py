from arshan.problem_7_p_1_arshan import Problem7P1Arshan


class Problem7P1Var1Arshan(object):
    def merge_two_sorted_dllists(self, it_a, it_b):
        sorted = Problem7P1Arshan().merge_two_sorted_llists(it_a, it_b)
        it = sorted
        prev = None
        while it:
            it.previous = prev
            prev = it
            it = it.next
        return sorted
