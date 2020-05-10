'''
  Find the first occurrence of an element greater than k in A.

  * if k is one of the keys in the array, then it's easy - all we need is to find its last occurrence and then return the next index.
'''


# time: O(log n)
# space: O(1)
def naive_search_first_occurrence_of_element_greater_than_k(arr, k):
    lower, upper = 0, len(arr) - 1
    adjusted_k = k

    while adjusted_k not in arr and arr[upper] > adjusted_k:
        adjusted_k += 1

    last_occurrence_of_k = -1

    while lower <= upper:
        midpoint = lower + (upper - lower) // 2

        if adjusted_k < arr[midpoint]:
            upper = midpoint - 1
        elif adjusted_k > arr[midpoint]:
            lower = midpoint + 1
        else:
            last_occurrence_of_k = midpoint
            lower = midpoint + 1

    return last_occurrence_of_k + 1 if adjusted_k == k else last_occurrence_of_k


# iterative approach using binary search
# time: O(log n)
# space: O(1)
def better_search_first_occurrence_of_element_greater_than_k(arr, k):
    lower, upper = 0, len(arr) - 1
    first_occurrence_of_next_greater_element = -1

    while lower <= upper:
        midpoint = lower + (upper - lower) // 2

        if k < arr[midpoint]:
            first_occurrence_of_next_greater_element = midpoint
            upper = midpoint - 1
        else:
            lower = midpoint + 1

    return first_occurrence_of_next_greater_element
