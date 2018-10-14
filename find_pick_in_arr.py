'''
given an array, first part is i ascending order, second part is in descending order.
write a function wich returns pick of array. You can not use max function
>>> find_pick([2, 5, 6, 19, 20, 22, 23, 31, 29, 15, 10, 6, 2])
31
>>> find_pick([1, 2, 1])
2

'''


def find_pick(lst):
    left = 0
    right = len(lst) - 1

    pivot_indx = len(lst) // 2
    
    while True:
        if lst[pivot_indx] > lst[pivot_indx -1] and lst[pivot_indx] > lst[pivot_indx +1]:
            break
        elif lst[pivot_indx] > lst[pivot_indx -1] and lst[pivot_indx] < lst[pivot_indx +1]:
            left = pivot_indx
            pivot_indx = (left + right) // 2
        elif lst[pivot_indx] < lst[pivot_indx -1] and lst[pivot_indx] > lst[pivot_indx + 1]:
            right = pivot_indx
            pivot_indx = (left + right) // 2
        
    return lst[pivot_indx]


        
if __name__ == '__main__':
    import doctest

    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. GREAT WORK!\n")       