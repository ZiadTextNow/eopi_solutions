from protocol.problem_5_p_1_var1 import Problem5P1Var1


class Problem5P1Var1Arshan(Problem5P1Var1):
    """
    Problem requirements:
    Space: O(1)
    Time: O(n)
    I pretty much modified their bubble-sort-lookalike solution.
    Our tests have values other than just 0, 1, 2.
    """
    def three_val_partition(self, unpartitioned_list):
        RED, WHITE, BLUE = (None,) * 3
        A = unpartitioned_list
        i = 0
        for k in range(len(A)):
            if not RED:
                RED = A[k]
            if A[k] == RED:
                A[i], A[k] = A[k], A[i]
                i += 1
        i = len(A) - 1
        for k in reversed(range(len(A))):
            if not BLUE:
                BLUE = A[k]
            if A[k] == RED:
                break
            if A[k] == BLUE:
                A[i], A[k] = A[k], A[i]
                i -= 1
