# from protocol.problem_5_p_1 import Problem5P1


class Problem5P1Ziad(object):
# class Problem5P1Ziad(Problem5P1):
    def dutch_flag_partition(self, pivot_index, unpartitioned_list):
        # return self.naive(pivot_index, unpartitioned_list)
        # return self.space_for_time(pivot_index, unpartitioned_list)
        # return self.one_pass(pivot_index, unpartitioned_list)
        return self.best_solution_from_eopi(pivot_index, unpartitioned_list)

    # Helper Function
    # not really needed, since Python allows you to do some cool swapping
    # out of the box, as I later found out
    def __swap(self, arr, lower_index, higher_index):
        temp = arr[lower_index]
        arr[lower_index] = arr[higher_index]
        arr[higher_index] = temp
        return arr

    # Brute force solution
    # time: O(n)
    # space: O(n)
    def naive(self, pivot_index, arr):
        pivot_value = arr[pivot_index]
        smaller_arr = []
        equal_arr = []
        greater_arr = []

        for element in arr:
            if element < pivot_value:
                smaller_arr.append(element)
            elif element == pivot_value:
                equal_arr.append(element)
            else:
                greater_arr.append(element)

        return smaller_arr + equal_arr + greater_arr

    # This approach uses 2 passes, one forward and one back.
    # We can choose to improve the brute force solution with better space, but at the cost of time
    # Iterate through array, and for each element, perform another iteration and swap the element
    # sacrifice runtime for better space efficiency
    # time: O(n^2)
    # space: O(1)
    def space_for_time(self, pivot_index, arr):
        pivot_value = arr[pivot_index]

        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                if arr[j] < pivot_value:
                    arr = self.swap(arr, i, j)
                    break

        for i in reversed(range(len(arr))):
            if arr[i] < pivot_value:
                break

            for j in reversed(range(len(i))):
                if arr[j] > pivot_value:
                    arr = self.__swap(arr, i, j)
                    break

    # This approach uses only a single pass.
    # time: O(n)
    # space: O(n)
    def one_pass(self, pivot_index, arr):
        pivot_value = arr[pivot_index]
        smaller_than_pivot = 0

        for i in range(len(arr)):
            if arr[i] < pivot_value:
                arr = self.__swap(arr, i, smaller_than_pivot)
                smaller_than_pivot += 1

        larger_than_pivot = len(arr) - 1
        for i in reversed(range(len(arr))):
            if arr[i] < pivot_value:
                break
            elif arr[i] > pivot_value:
                arr = self.__swap(arr, i, larger_than_pivot)
                larger_than_pivot -= 1

    # Similar to one_pass(), but we claim some more efficiency here
    # by classifying the elements of the array in a single pass using 4 subarrays
    # time: O(n)
    # space: O(1)
    def best_solution_from_eopi(self, pivot_index, arr):
        pivot_value = arr[pivot_index]
        smaller, equal, larger = 0, 0, len(arr)

        # i.e. keep iterating until no unclassified elements are left
        while equal < larger:
            if arr[equal] < pivot_value:
                arr = self.__swap(arr, smaller, equal)
                smaller += 1
                equal += 1
            elif arr[equal] == pivot_value:
                equal += 1
            else:
                larger -= 1
                arr = self.__swap(arr, larger, equal)
