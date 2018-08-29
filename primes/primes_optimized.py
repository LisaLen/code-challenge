"""Return count number of prime numbers, starting at 2.

For example::

    
    >>> primes(0)
    []

    >>> primes(1)
    [2]

    >>> primes(5)
    [2, 3, 5, 7, 11]

"""
def primes(count):
    """Return count number of prime numbers, starting at 2."""

    primes_lst = []

    n = 2
    while len(primes_lst) < count:
        is_prime = True
        for p in primes_lst:
            if n % p == 0:
                is_prime = False
                break
        if is_prime:
            primes_lst.append(n)
        n += 1
    return primes_lst






if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. GREAT WORK!\n")