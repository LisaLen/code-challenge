"""Find window of time when most authors were active.

For example::

    >>> data = [
    ...    ('Alice', 1901, 1950),
    ...    ('Bob',   1920, 1960),
    ...    ('Carol', 1908, 1945),
    ...    ('Dave',  1951, 1960),
    ... ]

    >>> most_active(data)
    (1920, 1945)

(Alice, Bob, and Carol were all active then).

If there's more than one period, find the earliest::

    >>> data = [
    ...    ('Alice', 1901, 1950),
    ...    ('Bob',   1920, 1960),
    ...    ('Carol', 1908, 1945),
    ...    ('Dave',  1951, 1960),
    ...    ('Eve',   1955, 1985),
    ... ]

    >>> most_active(data)
    (1920, 1945)

(Alice, Bob, Carol were active 1920-1945. Bob, Dave, and Eve were active 1951-1960.
Since there's a tie, the first was returned)
"""


def most_active(bio_data):
    """Find window of time when most authors were active."""
    start_most = 1901
    end_most = 1999

    most_active = (start_most,end_most,0)

    intersect = 0
    for d in bio_data:
        curr_s = d[1]
        curr_e = d[2]

        if curr_s > start_most and curr_s < end_most:
            start_most = curr_s
        if curr_e < end_most and curr_e > start_most:
            end_most = curr_e
        if curr_s > end_most:
            if intersect > most_active[2]:
                most_active = (start_most, end_most, intersect)
                start_most = curr_s
                end_most = curr_e
                intersect = 0
        else:
            intersect += 1



    return (most_active[0], most_active[1])


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. YAY!\n")