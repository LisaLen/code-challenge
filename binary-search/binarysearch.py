"""Using a binary search, find val in a range of 1-100. Return # of guesses.

Construct a list of 1-100 (inclusive). Write a binary search that searches
for val in that list (val will always be a number between 1 and 100).

Return the number of searches it took to find val. For a proper binary search
of 1-100, this should never be more than 7.

    >>> binary_search(50)
    1

    >>> binary_search(25)
    2

    >>> binary_search(75)
    2

    >>> binary_search(31) <= 7
    True

    
"""
from  random import randint

def binary_search(val):
    """Using binary search, find val in range 1-100. Return # of guesses."""

    assert 0 < val < 101, "Val must be between 1-100"

    num_guesses = 0

    max_l = 100
    min_l = 0

    
    while True:
        num_guesses += 1
        guess = int((max_l + min_l) / 2)
        

        if guess == val:
            return num_guesses

        elif guess < val:
            min_l = guess
        elif guess > val:
            max_l = guess

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. YOU'RE TERRIFIC AT THIS!\n")
