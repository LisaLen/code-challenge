"""Find the subsequence with the largest sum.

Given a list of integers, like:

  [1, 0, 3, -8, 4, -2, 3]

Return the contiguous subsequence with the largest sum. For
that example, the answer would be [4, -2, 3], which sums to 5.


    >>> largest_sum([1, 0, 3, -8, 4, -2, 3])
    [4, -2, 3]

    >>> largest_sum([1, 0, 3, -8, 4, -2, 3, -2])
    [4, -2, 3]

    >>> largest_sum([1, 0, 3, -8, 19, -20, 4, -2, 3, -2])
    [19]

For ties, return the first one:

    >>> largest_sum([2, 2, -10, 1, 3, -20])
    [2, 2]

Return the shortest version:

    >>> largest_sum([2, -2, 3, -1])
    [3]

If the list is all negative numbers, the subsequence
with the highest sum will be empty (ie, we can do no better
than pick nothing!):

    >>> largest_sum([-1, -2])
    []
"""


def largest_sum(nums):
    """Find subsequence with largest sum."""
    indx = 0
    max_sum = 0
    temp_sum = 0
    i = 0
    out = []

    while i < len(nums):
        temp_sum += nums[i]
        if temp_sum > max_sum:
            max_sum = temp_sum
            out = nums[indx:i+1]

        if temp_sum <= 0:
            if sum(nums[indx:i+1]) > max_sum:
                out = nums[indx:i+1]
            temp_sum = 0
            indx = i + 1
        i += 1

    return out








if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. YOU HANDLED THIS SUMMARILY!\n")
