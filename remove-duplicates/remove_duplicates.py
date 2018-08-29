""" Remove duplicates in a list

For example::

    >>> remove_duplicates([6, 9, 7, 9, 2, 6, 0])
    [6, 9, 7, 2, 0]

    >>> remove_duplicates([])
    []

    >>> remove_duplicates([6, 9, 7])
    [6, 9, 7]

"""


def remove_duplicates(items):
    """Remove duplicates in the list items and return that list."""
    if not items:
        return items

    check_set = set()

    i = 0
    while i < len(items):
        if items[i] in check_set:

            items.pop(i)
            continue
        check_set.add(items[i])
        i += 1
    return items
    
if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. GREAT WORK!\n")



