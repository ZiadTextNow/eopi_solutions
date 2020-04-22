import random
import collections


def iterative_bsearch(sorted_list, val):
    start = 0
    end = len(sorted_list) - 1
    while start <= end:
        # half_way_idx = (start + end) // 2   # this could cause overflow since start + end could be too large!
        half_way_idx = start + (end - start) // 2   # ending idx of the smaller valued list
        half_way_val = sorted_list[half_way_idx]
        if half_way_val == val:
            return half_way_idx
        elif val < half_way_val:
            end = half_way_idx - 1
        else:
            start = half_way_idx + 1
    return None


def recursive_bsearch(sorted_list, val):
    def bsearch_with_idxs(val, start, end):
        if end < start:
            return None
        half_way_idx = start + (end - start) // 2
        half_way_val = sorted_list[half_way_idx]
        if half_way_val == val:
            return half_way_idx
        elif val > half_way_val:
            return bsearch_with_idxs(val, half_way_idx + 1, end)
        else:
            return bsearch_with_idxs(val, start, half_way_idx - 1)
    return bsearch_with_idxs(val, 0, len(sorted_list) - 1)


if __name__ == "__main__":
    # sorted_list = [random.randint(0, 100) for _ in range(20)]
    # sorted_list.sort()
    sorted_list = [5, 10, 20, 40]
    print(sorted_list)
    print(iterative_bsearch(sorted_list, 5))
    print(iterative_bsearch(sorted_list, 10))
    print(iterative_bsearch(sorted_list, 20))
    print(iterative_bsearch(sorted_list, 40))
    print(recursive_bsearch(sorted_list, 5))
    print(recursive_bsearch(sorted_list, 10))
    print(recursive_bsearch(sorted_list, 20))
    print(recursive_bsearch(sorted_list, 40))
