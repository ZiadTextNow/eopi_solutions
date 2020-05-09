'''
  Test if p is a prefix of a string in an array of sorted string
'''


# notice how we can use bin search to make the problem smaller
# every run through the loop by simply comparing p with the string
# and if it doesn't contain it, move on.
def is_prefix(arr, p):
    lower, upper = 0, len(arr) - 1

    if arr is None:
        return False

    while lower <= upper:
        midpoint = lower + (upper - lower) // 2

        if p in arr[midpoint]:
            return True
        elif p < arr[midpoint]:
            upper = midpoint - 1
        else:
            lower = midpoint + 1

    return False
