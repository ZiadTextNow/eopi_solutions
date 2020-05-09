'''
  Find the interval where the first and last occurrence of k, and return it .
  e.g. for k = 1 and A = [0, 1, 1, 1, 1, 2] -> return [1, 4]
'''


# time: O(log n)
# space: O(1)
def first_last_interval(A, k):
    lower, upper = 0, len(A) - 1
    first_occurrence_of_k = -1
    last_occurrence_of_k = -1

    while lower <= upper:
        midpoint = lower + (upper - lower) // 2

        if k < A[midpoint]:
            upper = midpoint - 1
        elif k > A[midpoint]:
            lower = midpoint + 1
        else:
            first_occurrence_of_k = midpoint
            upper = midpoint - 1

    # reset lower and upper to their original values
    lower = first_occurrence_of_k if first_occurrence_of_k != -1 else 0
    upper = len(A) - 1

    # do the same but for last_occurrence_of_k
    while lower <= upper:
        midpoint = lower + (upper - lower) // 2

        if k < A[midpoint]:
            upper = midpoint - 1
        elif k > A[midpoint]:
            lower = midpoint + 1
        else:
            last_occurrence_of_k = midpoint
            lower = midpoint + 1

    return [first_occurrence_of_k, last_occurrence_of_k]


print(first_last_interval([1, 1, 2, 3, 5, 7, 7, 7, 7, 8, 9, 10], 11))