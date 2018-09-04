"""Convert a decimal number to binary representation.

For example::

    >>> dec2bin_backwards(0)
    '0'

    >>> dec2bin_backwards(1)
    '1'

    >>> dec2bin_backwards(2)
    '10'

    >>> dec2bin_backwards(4)
    '100'

    >>> dec2bin_backwards(15)
    '1111'

For example, using our alternate solution::

    >>> dec2bin_forwards(0)
    '0'

    >>> dec2bin_forwards(1)
    '1'

    >>> dec2bin_forwards(2)
    '10'

    >>> dec2bin_forwards(4)
    '100'

    >>> dec2bin_forwards(15)
    '1111'

And finally, using division:

    >>> dec2bin_division(0)
    '0'

    >>> dec2bin_division(1)
    '1'

    >>> dec2bin_division(2)
    '10'

    >>> dec2bin_division(4)
    '100'

    >>> dec2bin_division(15)
    '1111'


"""


def dec2bin_division(num):
    """Convert a decimal number to binary representation."""
    
    remainder = 0
    output = ''

    if  num == 0:
        return '0'

    if num == 1:
        return '1'

    while num != 1:
        remainder = num % 2
        output = str(remainder) + output
        num = num // 2
    output = str(num) + output
    
    return output



if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TEST PASSED. W00T!\n")
