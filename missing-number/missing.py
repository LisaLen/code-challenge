"""Given a list of numbers 1...max_num, find which one is missing in a list."""


def missing_number(nums, max_num):
    """Given a list of numbers 1...max_num, find which one is missing.

    *nums*: list of numbers 1..[max_num]; exactly one digit will be missing.
    *max_num*: Largest potential number in list

    >>> missing_number([7, 3, 2, 4, 5, 6, 1, 9, 10], 10)
    8
    
    """
    #runtime is O(n)
        # numbers = set()
        # for i in range(1, max_num +1):
        #     numbers.add(i)

        # for num in nums:
        #     if num in numbers:
        #         numbers.remove(num)
          
        # for num in numbers:
        #     print(num)

    
    # O(n) runtime and O(1) runspace

    sum1 = 0
    for num in nums:
        sum1 += num

    sum2 = 0

    for i in range(1, max_num+1):
        sum2 += i

    return sum2 - sum1





 
    


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASS. NICELY DONE!\n")
