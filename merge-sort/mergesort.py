"""Merge sort.
    

    >>> my_list     = [3, 4, 6, 10, 11, 15]
    >>> alices_list = [1, 5, 8, 12, 14, 19]
    >>> print(merge_lists(my_list, alices_list))
    [1, 3, 4, 5, 6, 8, 10, 11, 12, 14, 15, 19]

    >>> print(merge_lists([], []))
    []

    >>> print(merge_lists([1, 2, 3], []))
    [1, 2, 3]
    >>> print(merge_lists([], [4, 5, 6]))
    [4, 5, 6]
    >>> print(merge_lists([100], [4, 5, 6]))
    [4, 5, 6, 100]




    >>> nums = [3, 5, 10, 2, 1, 9, 7, 6, 4, 8]
    >>> sorted_nums = merge_sort(nums)
    >>> sorted_nums
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

"""


def merge_sort(lst):
    """Divide and conquer: reduce to lists of 0-1 items, then recombine."""
    
    
    if len(lst) <= 1:
        return lst
    if len(lst) == 2:
        return merge_lists(lst[:1],lst[1:])
    pivot = len(lst) // 2
    return merge_lists(merge_sort(lst[:pivot]), merge_sort(lst[pivot:]))




def merge_lists(lst1, lst2):

    if not lst1:
        return lst2[:]
    if not lst2:
        return lst1[:] 

    result = []
    i, j = 0, 0 

    while i < len(lst1) and j < len(lst2):
        if lst1[i] > lst2 [j]:
            result.append(lst2[j])
            j += 1
        else:
            result.append(lst1[i])
            i += 1
    if i == len(lst1):
        result.extend(lst2[j:])
    if j == len(lst2):
        result.extend(lst1[i:])

    return result



if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. AWESOME WORK!\n")
