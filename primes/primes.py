"""Return count number of prime numbers, starting at 2.

For example::

    >>> is_prime(3)
    True

    >>> is_prime(24)
    False

    >>> primes(0)
    []

    >>> primes(1)
    [2]

    >>> primes(5)
    [2, 3, 5, 7, 11]

"""
def is_prime(number):
    assert number >= 0

    if number < 2:
        return False

    if number == 2:
        return True

    if number % 2 == 0:
        return False

    n = 3

    while n*n < number:
        if number % n == 0: 
            return False
        n += 2
    return True
    

def primes(count):
    """Return count number of prime numbers, starting at 2."""
    numbers = []
    
    i = 2
    j = 0
    while j < count:
        if is_prime(i):
            numbers.append(i)
            j += 1
        i += 1
    return numbers





if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. GREAT WORK!\n")
