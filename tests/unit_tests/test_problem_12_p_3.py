import pytest
from vlad.problem_12_p_3_vlad import Problem12P3Vlad


class TestProblem12P3(object):
    def instantiate_solution(self):
        return Problem12P3Vlad()

    @pytest.mark.parametrize("cache_size, insert_books, expected_books", [
        (3, [(10**9 , 10.99), (10**9 + 1, 5.99), (10**9 + 2, 15.49)],
         [(10**9, 10.99), (10**9 + 1, 5.99), (10**9 + 2, 15.49)]),
        (3, [(10 ** 9, 10.99), (10 ** 9 + 1, 5.99), (10 ** 9 + 2, 15.49), (10 ** 9 + 3, 11.49)],
         [(10 ** 9 + 1, 5.99), (10 ** 9 + 2, 15.49), (10 ** 9 + 3, 11.49)]),
        (3, [(10 ** 9, 10.99), (10 ** 9 + 1, 5.99), (10 ** 9 + 2, 15.49), (10 ** 9 + 1, 11.49)],
         [(10 ** 9, 10.99), (10 ** 9 + 2, 15.49), (10 ** 9 + 1, 5.99)]),
        (3, [(10 ** 9, 10.99), (10 ** 9 + 1, 5.99), (10 ** 9 + 2, 15.49), (10 ** 9 + 1, 5.99)],
         [(10 ** 9, 10.99), (10 ** 9 + 2, 15.49), (10 ** 9 + 1, 5.99)]),
    ])
    def test_insert(self, cache_size, insert_books, expected_books):
        isbn_cache = self.instantiate_solution().ISBNCache(cache_size)
        for book in insert_books:
            isbn_cache.insert(book)
        assert isbn_cache.get_list_of_books_in_priority_order() == expected_books

    @pytest.mark.parametrize("cache_size, insert_books, lookup_books, expected_lookup_books_results, expected_books", [
        (3, [(10 ** 9, 10.99), (10 ** 9 + 1, 5.99), (10 ** 9 + 2, 15.49)], [10 ** 9], [10.99],
         [(10 ** 9 + 1, 5.99), (10 ** 9 + 2, 15.49), (10 ** 9, 10.99)]),
        (3, [(10 ** 9, 10.99), (10 ** 9 + 1, 5.99), (10 ** 9 + 2, 15.49)], [10 ** 9 + 2], [15.49],
         [(10 ** 9, 10.99), (10 ** 9 + 1, 5.99), (10 ** 9 + 2, 15.49)]),
        (3, [(10 ** 9, 10.99), (10 ** 9 + 1, 5.99), (10 ** 9 + 2, 15.49)], [10 ** 9 + 3], [False],
         [(10 ** 9, 10.99), (10 ** 9 + 1, 5.99), (10 ** 9 + 2, 15.49)]),
        (3, [(10 ** 9, 10.99), (10 ** 9 + 1, 5.99), (10 ** 9 + 2, 15.49)], [10 ** 9, 10 ** 9 + 1], [10.99, 5.99],
         [(10 ** 9 + 2, 15.49), (10 ** 9, 10.99), (10 ** 9 + 1, 5.99)]),
    ])
    def test_lookup(self, cache_size, insert_books, lookup_books, expected_lookup_books_results, expected_books):
        isbn_cache = self.instantiate_solution().ISBNCache(cache_size)
        for book in insert_books:
            isbn_cache.insert(book)
        lookup_books_results = []
        for lookup_book in lookup_books:
            lookup_books_results.append(isbn_cache.lookup(lookup_book))
        assert lookup_books_results == expected_lookup_books_results
        assert isbn_cache.get_list_of_books_in_priority_order() == expected_books

    @pytest.mark.parametrize("cache_size, insert_books, remove_books, expected_books", [
        (3, [(10 ** 9, 10.99), (10 ** 9 + 1, 5.99), (10 ** 9 + 2, 15.49)], [10 ** 9],
         [(10 ** 9 + 1, 5.99), (10 ** 9 + 2, 15.49)]),
        (3, [(10 ** 9, 10.99), (10 ** 9 + 1, 5.99), (10 ** 9 + 2, 15.49)], [10 ** 9, 10 ** 9 + 2],
         [(10 ** 9 + 1, 5.99)]),
        (3, [(10 ** 9, 10.99), (10 ** 9 + 1, 5.99), (10 ** 9 + 2, 15.49)], [10 ** 9, 10 ** 9 + 2, 10 ** 9 + 1],
         []),
    ])
    def test_remove(self, cache_size, insert_books, remove_books, expected_books):
        isbn_cache = self.instantiate_solution().ISBNCache(cache_size)
        for book in insert_books:
            isbn_cache.insert(book)
        for remove_book in remove_books:
            isbn_cache.remove(remove_book)
        assert isbn_cache.get_list_of_books_in_priority_order() == expected_books
