import random

if __name__ == '__main__':

    def func_that_deals_with_lists(the_list):
        the_list += [7]

    some_list = [1]
    func_that_deals_with_lists(some_list)
    print(some_list)

    def func_that_deals_with_dicts(the_dict):
        the_dict = {
            'blah': the_dict
        }

    some_dict = {
        'boo': 'fee'
    }
    func_that_deals_with_dicts(some_dict)
    print(some_dict)
