'''
  Approach 1 is to do a linear search through array (trivial)

  Approach 2 is to use binary search
    . at every midpoint, look @ left and right values, we are interested in 3 possibilities:
        -> midpoint element is smaller than both of its neighbors
          -> must be a local minimum
        -> midpoint element is larger than its left neighbor
          -> there might be a local local minimum in the left half, so binary search it
        -> midpoint element is larger than its right neighbor
          -> there might be a local minimum in the right half, so binary search it
'''


def local_minimum(arr):
    lower, upper = 0, len(arr) - 1

    while lower <= upper:
        midpoint = lower + (upper - lower) // 2

        if arr[midpoint] < arr[midpoint - 1] and arr[midpoint] < arr[midpoint + 1]:
            return midpoint
        elif arr[midpoint] > arr[midpoint - 1]:
            upper = midpoint - 1
        else:
            lower = midpoint + 1

    return -1
