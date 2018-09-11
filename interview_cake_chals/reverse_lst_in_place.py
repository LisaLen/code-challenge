'''Write a function that takes a list of characters and 
reverses the letters in place.
    >>> my_list = ['a', 'b', 'c', 'd']
    >>> new_list = reverse(my_list)
    >>> new_list
    ['d', 'c', 'b', 'a']
    >>> my_list is new_list
    True
    >>> reverse([1, 2, 3, 4, 5])
    [5, 4, 3, 2, 1]

'''

def reverse(lst):

    
    for i in range(len(lst) // 2):
        lst[i], lst[-1-i] = lst[-1-i], lst[i]
    return lst


if __name__ == '__main__':
    import doctest

    if doctest.testmod().failed == 0:
        print('\n*** All Tests Passed, Good Work!***\n')