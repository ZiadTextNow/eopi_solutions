from protocol.problem_5_p_1_var3 import Problem5P1Var3


class Problem5P1Var3Arshan(Problem5P1Var3):
    def bool_val_partition(self, unpartitioned_list):
        A = unpartitioned_list
        i = 0
        for j in range(len(A)):
            if not A[j]:
                A[i], A[j] = A[j], A[i]
                i += 1
