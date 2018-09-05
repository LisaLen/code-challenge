"""Given a list, sort it using insertion sort.

For example::

    >>> from random import shuffle
    >>> alist = list(range(1, 11))

    >>> shuffle(alist)
    >>> insertion_sort(alist)
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    >>> shuffle(alist)
    >>> insertion_sort(alist)
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    >>> shuffle(alist)
    >>> insertion_sort(alist)
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
"""


def insertion_sort(alist):
    """Given a list, sort it using insertion sort."""
    i = 1
    while i < len(alist):
        j = i
        while j > 0 and alist[j]< alist[j-1]:
            alist[j], alist[j-1] = alist[j-1], alist[j]
            j -= 1
        i += 1
    return alist


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. NICE SORTING!\n")
