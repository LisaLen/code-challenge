"""Merge sort.
    
    >>> nums = [3, 5, 10, 2, 1, 9, 7, 6, 4, 8]
    >>> merge_sort(nums)
    >>> nums
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

"""

def merge_sort(lst):
    if len(lst) > 1:

        mid = len(lst) // 2

        left = lst[:mid]
        right = lst[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = lst_indx = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                lst[lst_indx] = left[i]
                i += 1
            else:
                lst[lst_indx] = right[j]
                j += 1
            lst_indx += 1

        while i < len(left):
            lst[lst_indx] = left [i]
            lst_indx += 1
            i += 1
        while j < len(right):
            lst[lst_indx] = right[j]
            lst_indx += 1
            j += 1


if __name__ == '__main__':
    import doctest

    if doctest.testmod().failed == 0:
        print('\n***TESTS PASSED***\n')