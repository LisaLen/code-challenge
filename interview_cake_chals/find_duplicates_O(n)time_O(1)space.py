'''In Find a duplicate, Space Edition™, we were given a list of integers where:

the integers are in the range 1..n1..n
the list has a length of n+1n+1
These properties mean the list must have at least 1 duplicate. Our challenge was to find a duplicate number, while optimizing for space. We used a divide and conquer approach, iteratively cutting the list in half to find a duplicate integer in O(n\lg{n})O(nlgn) time and O(1)O(1) space (sort of a modified binary search).

But we can actually do better. We can find a duplicate integer in O(n)O(n) time while keeping our space cost at O(1)O(1).

This is a tricky one to derive (unless you have a strong background in graph theory), so we'll get you started:

Imagine each item in the list as a node in a linked list. In any linked list, ↴ each node has a value and a "next" pointer. In this case:

The value is the integer from the list.
The "next" pointer points to the value-eth node in the list (numbered starting from 1). For example, if our value was 3, the "next" node would be the third node.


>>> find_duplicate([3, 4, 2, 3, 1, 5])
3
>>> find_duplicate([3, 1, 2, 2])
2
>>> find_duplicate([4, 3, 1, 1, 4])
4

'''
def find_duplicate(lst):
    n = len(lst) - 1

#FIND the item in cycle
#start at the head of linkedList(which is last element of lst) and goung n steps forward. 
#nth items would be inside of the loop

    position_in_cycle = n + 1
    for i in range(n):
        position_in_cycle = lst[position_in_cycle-1]    

    #count lenth of the cycle
    remember_position_in_cycle = position_in_cycle
    current_position_in_cycle = lst[position_in_cycle-1]
    cycle_step_count = 1

    while current_position_in_cycle != remember_position_in_cycle:
        current_position_in_cycle = lst[current_position_in_cycle-1]
        cycle_step_count += 1

    #Find the first node in cycle
    pointer_start = n + 1
    pointer_ahead = n + 1

    for i in range(cycle_step_count):
        pointer_ahead = lst[pointer_ahead-1]
    while pointer_start != pointer_ahead:
        pointer_start = lst[pointer_start - 1]
        pointer_ahead = lst[pointer_ahead - 1]

    return pointer_start

if __name__ == '__main__':
    import doctest

    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. GREAT WORK!\n")