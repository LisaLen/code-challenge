'''Find a duplicate, Space Edition™.

We have a list of integers, where:

The integers are in the range 1..n1..n
The list has a length of n+1n+1
It follows that our list has at least one integer which appears at least twice. 
But it may have several duplicates, and each duplicate may appear more than twice.

Write a function which finds an integer that appears more than once in our list.
 (If there are multiple duplicates, you only need to find one of them.)

We're going to run this function on our new, super-hip MacBook Pro With Retina
 Display™. Thing is, the damn thing came with the RAM soldered right to the 
 motherboard, so we can't upgrade our RAM. So we need to optimize for space!

>>> find_duplicate([1, 2, 1, 3, 4, 6, 5])
1
>>> find_duplicate([1,1])
1

 '''

def find_duplicate(lst):

    floor = 1
    ceiling = len(lst) - 1

    while floor < ceiling:
        mid = floor + (ceiling - floor) // 2
        # found to ranges of numbers floor... mid, mid+1 ... ceiling


        numbers_in_lower_range = 0
        lower_floor = floor
        lower_ceiling = mid

        for item in lst:
            if item >= lower_floor and item <= lower_ceiling:
                numbers_in_lower_range += 1

        lower_range_len = lower_ceiling - lower_floor + 1

        if numbers_in_lower_range > lower_range_len:
            ceiling = lower_ceiling
        else:
            floor = lower_floor

    return ceiling











if __name__ =='__main__':
    import doctest

    if doctest.testmod().failed == 0:
        print('\n***PASSED***\n')
