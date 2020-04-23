from protocol.problem_5_p_6_var1 import Problem5P6Var1


class Problem5P6Var1Arshan(Problem5P6Var1):
    def find_longest_equal_sublist(self, int_list):
        return self.max_so_far_with_lookup(int_list)
        return self.brute_force_with_lookup(int_list)

    def max_so_far_with_lookup(self, int_list):
        m = 0
        A = int_list
        l = {}
        for i in A:
            if i not in l:
                l[i] = 0
            l[i] += 1
            m = max(m, l[i])
        return m

    def brute_force_with_lookup(self, input_list):
        A = input_list
        l = {}
        for i in A:
            if i not in l:
                l[i] = 0
            l[i] += 1
        return max([l[k] for k in l])
