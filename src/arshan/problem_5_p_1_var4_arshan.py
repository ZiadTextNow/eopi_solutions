from protocol.problem_5_p_1_var4 import Problem5P1Var4


class Problem5P1Var4Arshan(Problem5P1Var4):
    def bool_val_keep_true_order_partition(self, unpartitioned_list):
        A = unpartitioned_list
        i = len(A) - 1
        for k in reversed(range(len(A))):
            if A[k]:
                A[i], A[k] = A[k], A[i]
                i -= 1
