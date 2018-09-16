'''
Given a list of integers, find the highest product you can get from three of the integers.

The input list_of_ints will always have at least three integers.

>>> highest_product([5, 6, 1, 8, 13, 12, 10])
1560

>>> highest_product([-10, -10, 1, 3, 2])
300

'''
def highest_product(lst_int):

    a = lst_int[0]
    b = lst_int[1]
    c = lst_int[2]

    if len(lst_int) == 3:
        return a * b * c

    first = max(a, b, c)
    third = min(a, b, c)
    second = a + b + c - first - third

    for i in range(3, len(lst_int)):
        if lst_int[i] > first:
            third = second
            second = first
            first = lst_int[i]
        elif lst_int[i] > second:
            third = second
            second = lst_int[i]
        elif lst_int[i] > third:
            third = lst_int[i]
        else:
            continue

    return first * second * third



if __name__ == '__main__':
    import doctest

    if doctest.testmod().failed == 0:
        print('\n***TEST PASSES***\n')
