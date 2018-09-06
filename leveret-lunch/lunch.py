"""Leveret lunch count.

Check that garden is valid::

    >>> garden = [
    ...     [1, 1],
    ...     [1],
    ... ]

    >>> lunch_count(garden)
    Traceback (most recent call last):
    ...
    AssertionError: Garden not a matrix!

    >>> garden = [
    ...     [1, 1],
    ...     [1, 'a'],
    ... ]

    >>> lunch_count(garden)
    Traceback (most recent call last):
    ...
    AssertionError: Garden values must be ints!

Consider simple cases::

    >>> garden = [
    ...     [0, 0, 0],
    ...     [0, 0, 0],
    ...     [0, 0, 0]
    ... ]

    >>> lunch_count(garden)
    0

    >>> garden = [
    ...     [1, 1, 1],
    ...     [0, 1, 1],
    ...     [9, 1, 9]
    ... ]

    >>> lunch_count(garden)
    3

    >>> garden = [
    ...     [1, 1, 1],
    ...     [1, 1, 1],
    ...     [1, 1, 1]
    ... ]

    >>> lunch_count(garden)
    9

Make sure it works with even-sides
(this will start with the 4 and head east)::

    >>> garden = [
    ...     [9, 9, 9, 9],
    ...     [9, 3, 1, 0],
    ...     [9, 1, 4, 2],
    ...     [9, 9, 1, 0],
    ... ]

    >>> lunch_count(garden)
    6

Consider our most complex case::

    >>> garden = [
    ...     [2, 3, 1, 4, 2, 2, 3],
    ...     [2, 3, 0, 4, 0, 3, 0],
    ...     [1, 7, 0, 2, 1, 2, 3],
    ...     [9, 3, 0, 4, 2, 0, 3],
    ... ]

    >>> lunch_count(garden)
    15

"""


def lunch_count(garden):
    """Given a garden of nrows of ncols, return carrots eaten."""

    # Sanity check that garden is valid

    row_lens = [len(row) for row in garden]
    assert min(row_lens) == max(row_lens), "Garden not a matrix!"
    assert all(all(type(c) is int for c in row) for row in garden), \
        "Garden values must be ints!"

    # Get number of rows and columns

    nrows = len(garden)
    ncols = len(garden[0])

    #find start point (x, y)
    x = nrows // 2
    y = ncols // 2
    options = [(x,y)]
  
    if nrows % 2 == 0  and x - 1 >= 0:
        options.append((x-1, y))

    if ncols % 2 == 0 and y - 1 >= 0:
        options.append((x, y - 1))

    if x - 1 >=0 and y - 1 >= 0:
        options.append((x-1, y-1))
 
    #print('start options', options)
  
    all_carrots = 0
    
    while True:
        max_carrots = 0
        for o in options:
            if garden[o[0]][o[1]] > max_carrots:
                
                max_carrots = garden[o[0]][o[1]]
                x = o[0]
                y = o[1]
        if max_carrots == 0:
            break
        all_carrots += max_carrots
        garden[x][y] = 0
       
        options = []
        
        if y - 1 >= 0:
            options.append((x, y-1))
        if x - 1 >= 0:
            options.append((x-1, y))
        if y + 1 < ncols:
            options.append((x, y + 1))
        if x + 1 < nrows:
            options.append((x + 1, y))

   return all_carrots


if __name__ == '__main__':
    import doctest

    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASS! HOP ALONG NOW!\n")
