from protocol.problem_12_p_3 import Problem12P3
import collections

"""
THINGS TO NOTE ABOUT THIS PROBLEM

collections.OrderedDict is an absolute beauty! Its a mapped hash table with order implemented as linked list to keep 
track of order and since it's a linked list removal is O(1) unlike array since elements don't have to be shifted!
"""


class Problem12P3Vlad(Problem12P3):
    """
    This is only better that using a queue on its own for looking up if the value is already in the queue or not. This
    does not help us find where in the queue it is. So only faster for cases that the item is not in the queue if it
    occurs oftem at the expense of 2n more space
    """
    class HashQueue(Problem12P3.ISBNCache):
        def __init__(self, cache_size):
            self.cache_size = cache_size
            self.cur_size = 0
            self.priority_queue = collections.deque([], self.cache_size)
            self.book_dict = {}

        def insert(self, book):  # note that book[0] is ISBN and book[1] is price
            if self.book_dict.get(book[0]):
                self.priority_queue.remove(book[0])
                self.priority_queue.append(book[0])
            else:
                if self.cur_size == self.cache_size:
                    del self.book_dict[self.priority_queue.popleft()]
                    self.cur_size -= 1
                self.book_dict[book[0]] = book[1]
                self.priority_queue.append(book[0])
                self.cur_size += 1

        def lookup(self, isbn):
            if isbn in self.priority_queue:
                self.priority_queue.remove(isbn)
                self.priority_queue.append(isbn)
                return self.book_dict[isbn]
            return False

        def remove(self, isbn):
            if self.book_dict.get(isbn):
                self.priority_queue.remove(isbn)
                del self.book_dict[isbn]

        def get_list_of_books_in_priority_order(self):
            return_list = []
            for isbn in self.priority_queue:
                return_list.append((isbn, self.book_dict[isbn]))
            return return_list

    class BookSoln(Problem12P3.ISBNCache):
        def __init__(self, cache_size):
            self._isbn_price_table = collections.OrderedDict()
            self.cache_size = cache_size

        def insert(self, book):
            price = book[1]
            if book[0] in self._isbn_price_table:
                price = self._isbn_price_table.pop(book[0])
            elif len(self._isbn_price_table) >= self.cache_size:
                """
                this step removes the least recently used element in the queue. It is important to not that since this
                would need to be implemented as a linked list for efficient removals (pop() method above) when removing
                the least recently used (this would be like head of linked list) the list nodes should have an attribute
                isbn as well efficiently remove the dict key otherwise all dict values would have to be searched until 
                the linked list node that was removed is found
                """
                self._isbn_price_table.popitem(last=False)
            self._isbn_price_table[book[0]] = price

        def lookup(self, isbn):
            if isbn not in self._isbn_price_table:
                return False
            price = self._isbn_price_table.pop(isbn)
            self._isbn_price_table[isbn] = price
            return price

        def remove(self, isbn):
            self._isbn_price_table.pop(isbn, None)

        def get_list_of_books_in_priority_order(self):
            return_list = []
            for isbn, price in self._isbn_price_table.items():
                return_list.append((isbn, price))
            return return_list

    class ISBNCache(HashQueue):
    # class ISBNCache(BookSoln):
        pass
