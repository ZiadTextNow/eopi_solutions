from protocol.problem_10_p_1 import Problem10P1


class Problem10P1Arshan(Problem10P1):
    def merge_sorted_lists(self, *stock_price_lists):
        return self.better_solution(*stock_price_lists)
        return self.naive_solution(*stock_price_lists)

    def naive_solution(self, *stock_price_lists):
        sorted_list = []
        for l in stock_price_lists[0]:
            for item in l:
                inserted = False
                for i, it in enumerate(sorted_list):
                    if item < it:
                        inserted = True
                        sorted_list.insert(i, item)
                        break
                if not inserted:
                    sorted_list.append(item)
        return sorted_list

    def better_solution(self, *stock_price_lists):
        def merge_two_lists(l1, l2):
            merged = []
            while l1 or l2:
                if not l1 or not l2:
                    merged += l1 or l2
                    break
                it1, it2 = l1[0], l2[0]
                if it1 < it2:
                    merged.append(it1)
                    l1.pop(0)
                else:
                    merged.append(it2)
                    l2.pop(0)
            return merged
        merged = []
        for l in stock_price_lists[0]:
            merged = merge_two_lists(l, merged)
        return merged

