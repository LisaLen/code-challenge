'''I opened up a dictionary to a page in the middle and started flipping through,
looking for words I didn't know. I put each word I didn't know at increasing 
indices in a huge list I created in memory. When I reached the end of the 
dictionary, I started from the beginning and did the same thing until I reached 
the page I started at.

Now I have a list of words that are mostly alphabetical, except they start 
somewhere in the middle of the alphabet, reach the end, and then start from the 
beginning of the alphabet. In other words, this is an alphabetically ordered 
list that has been "rotated." For example:

    >>> find_rotation_point(['ptolemaic', 'retrograde', 'supplant', 'undulate', 'xenoepist', 'asymptote', 'babka', 'banoffee', 'engender', 'karpatka', 'othellolagkage'])
    5

Write a function for finding the index of the "rotation point," which is where 
I started working from the beginning of the dictionary. This list is huge 
(there are lots of words I don't know) so we want to be efficient here.'''

def find_rotation_point(lst):
    '''return index of rotation point'''

    if not lst:
        return

    floor_indx = 0
    ceiling_indx = len(lst) - 1
    

    while (ceiling_indx - floor_indx) > 1:
        middle_indx = (ceiling_indx - floor_indx) // 2 + floor_indx
        if lst[middle_indx] < lst[ceiling_indx]:
            ceiling_indx = middle_indx
        else:
            floor_indx = middle_indx
    
    if lst[floor_indx] < lst[ceiling_indx]:
        return floor_indx
    return ceiling_indx

    

if __name__ =='__main__':
    import doctest

    if doctest.testmod().failed == 0:
        print('\n***PASSED***\n')