class Problem11P1Arshan(object):
    def first_occurrence_of_k(self, sorted_list, k):
        return self.clean_version(sorted_list, k)

    def dirty_version(self, sorted_list, k):
        b, e = 0, len(sorted_list) - 1
        i = len(sorted_list) >> 1
        while True:
            if k < sorted_list[i]:
                e = i
                i -= ((e - b) >> 1)
            elif sorted_list[i] < k:
                b = i
                i += ((e - b) >> 1)
            else:
                if sorted_list[i - 1] == sorted_list[i]:
                    e = i
                    i -= ((e - b) >> 1)
                else:
                    return i
            if e - b <= 1:
                if sorted_list[b] == k:
                    return b
                if sorted_list[e] == k:
                    return e
                return -1

    def clean_version(self, sorted_list, k):
        b, e = 0, len(sorted_list) - 1
        while True:
            i = b + ((e - b) >> 1)
            v = sorted_list[i]
            b = i if v < k else b
            e = i if k <= v else e
            if e - b <= 1:
                if sorted_list[b] == k:
                    return b
                if sorted_list[e] == k:
                    return e
                return -1
