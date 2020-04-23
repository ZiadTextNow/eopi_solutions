from protocol.problem_5_p_1_var2 import Problem5P1Var2


class Problem5P1Var2Arshan(Problem5P1Var2):
    def four_val_partition(self, unpartitioned_list):
        RED, WHITE, BLUE, GREEN = (None, ) * 4
        A = unpartitioned_list
        i = 0
        for k in range(len(A)):
            if not RED:
                RED = A[k]
            if A[k] == RED:
                A[i], A[k] = A[k], A[i]
                i += 1
        i = k = len(A) - 1
        for k in reversed(range(len(A))):
            if not GREEN:
                GREEN = A[k]
            if A[k] == RED:
                break
            if A[k] == GREEN:
                A[i], A[k] = A[k], A[i]
                i -= 1
        i = k + 1
        for k in range(i, len(A)):
            if not WHITE:
                WHITE = A[k]
            if A[k] == GREEN:
                break
            if A[k] == WHITE:
                A[i], A[k] = A[k], A[i]
                i += 1
