import collections


def find_anagrams(dictionary):
    sorted_string_to_anagrams = collections.defaultdict(list)
    for s in dictionary:
        sorted_string_to_anagrams[''.join(sorted(s))].append(s)  # join had to be used since sort returns list
    return [group for group in sorted_string_to_anagrams.values() if len(group) > 1]


# I had to use a tuple here of size 26 for all the letters since I couldn't use a dict as a key
def fast_find_anagrams(dictionary):
    letter_count_to_anagrams = collections.defaultdict(list)
    for s in dictionary:
        letter_count_to_anagrams[count_num_of_each_letter_in_tuple(s)].append(s)
    return [group for group in letter_count_to_anagrams.values() if len(group) > 1]


"""
this used less memory since we don't have to use a 26 letter list. We can convert the dict to a list of tuples and then
to a frozenset so that it is hashable and can be used as a key that doesn't care about order
"""
def fast_find_anagrams_with_dict(dictionary):
    letter_count_to_anagrams = collections.defaultdict(list)
    for s in dictionary:
        key = frozenset(count_num_of_each_letter(s).items())
        letter_count_to_anagrams[key].append(s)
    return [group for group in letter_count_to_anagrams.values() if len(group) > 1]


def fast_find_anagrams_with_hash_class(dictionary):
    letter_count_to_anagrams = collections.defaultdict(list)
    for s in dictionary:
        key = LetterCount(count_num_of_each_letter(s))
        letter_count_to_anagrams[key].append(s)
    return [group for group in letter_count_to_anagrams.values() if len(group) > 1]


# wowawewa
def count_num_of_each_letter_with_offset(s, offset):
    def constant_factory(value):
        return lambda: value
    d = collections.defaultdict(constant_factory(offset))
    for l in s:
        d[l] += 1
    return d


# amazing!!!
def count_num_of_each_letter(s):
    d = collections.defaultdict(int)
    for l in s:
        d[l] += 1
    return d


def count_num_of_each_letter_in_tuple(s):
    result = [0] * 26
    start = ord('a')
    for l in s:
        list_idx = ord(l) - start
        result[list_idx] += 1
    return tuple(result)


# lame
def old_count_num_of_each_letter(s):
    d = {}
    for l in s:
        if d.get(l) is not None:
            d[l] += 1
        else:
            d[l] = 1
    return d


class LetterCount(object):
    def __init__(self, letter_count_dict):
        self.letter_count_dict = letter_count_dict

    def __hash__(self):
        return hash(frozenset(self.letter_count_dict.items()))

    def __eq__(self, other):
        return set(self.letter_count_dict.items()) == set(other.letter_count_dict.items())


class ContactList(object):
    def __init__(self, names):
        self.names = names

    def __hash__(self):
        return hash(frozenset(self.names))

    def __eq__(self, other):
        return set(self.names) == set(other.names)


def merge_contact_lists(contacts):
    return list(set(contacts))


if __name__ == "__main__":
    s = 'mississauga'
    print(count_num_of_each_letter(s))
    print(old_count_num_of_each_letter(s))
    print(count_num_of_each_letter_with_offset(s, 1))
    print(count_num_of_each_letter_with_offset(s, 0) == count_num_of_each_letter(s))
    print(count_num_of_each_letter_in_tuple(s))

    input = ['debitcard', 'elvis', 'silent', 'badcredit', 'lives', 'freedom', 'listen', 'levis', 'money']
    print(f'\n#############################################\n')
    print(find_anagrams(input))
    print(fast_find_anagrams(input))
    print(fast_find_anagrams_with_dict(input))
    print(fast_find_anagrams_with_hash_class(input))

    print(f'\n#############################################\n')
    c1 = ContactList(['a', 'b', 'c', 'a'])
    c2 = ContactList(['b', 'c', 'd', 'b'])
    c3 = ContactList(['b', 'c', 'a'])
    print(merge_contact_lists([c1, c2, c3]))
