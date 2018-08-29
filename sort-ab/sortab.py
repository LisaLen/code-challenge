"""Given already-sorted lists, `a` and `b`, return sorted list of both.

You may not use sorted() or .sort().

Check edge cases of empty lists:

    >>> sort_ab([], [])
    []

    >>> sort_ab([1, 2,3], [])
    [1, 2, 3]

    >>> sort_ab([], [1, 2, 3])
    [1, 2, 3]

Check:

    >>> sort_ab([1, 3, 5, 7], [2, 6, 8, 10])
    [1, 2, 3, 5, 6, 7, 8, 10]
    >>> sort_ab([1, 1, 5, 7], [2, 2, 8, 10])
    [1, 1, 2, 2, 5, 7, 8, 10]
"""


def sort_ab(a, b):
    """Given already-sorted lists, `a` and `b`, return sorted list of both.

    You may not use sorted() or .sort().
    """
    if not a and not b:
        return []

    i, j = 0, 0
    sorted_lst = []
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            sorted_lst.append(a[i])
            i += 1
        else:
            sorted_lst.append(b[j])
            j += 1
        

    if i >= len(a):
        sorted_lst.extend(b[j:])
    if j >= len(b):
        sorted_lst.extend(a[i:])

    return sorted_lst


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. YOU'RE A MERGE CHAMPION!!\n")
