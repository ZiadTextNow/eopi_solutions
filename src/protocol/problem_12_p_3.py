from protocol.errors import EOPINotImplementedError


class Problem12P3(object):
    class ISBNCache(object):
        def lookup(self, isbn):
            raise EOPINotImplementedError()

        def insert(self, book):
            raise EOPINotImplementedError()

        def remove(self, isbn):
            raise EOPINotImplementedError()

        """
        This is so that testing can be done easily.
        For example if the inserts were (1234567890, 10.99), (1111111111, 5.99), (2222211111, 15.49) then this method
        would return the following list: [(1234567890, 10.99), (1111111111, 5.99), (2222211111, 15.49)] where leftmost
        elements in the list are least recently used and rightmost are most recently used
        """
        def get_list_of_books_in_priority_order(self):
            raise EOPINotImplementedError()
