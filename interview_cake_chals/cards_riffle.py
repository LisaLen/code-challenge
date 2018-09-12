'''write a function to tell us if a full deck of cards shuffled_deck is a single
 riffle of two other halves half1 and half2.

>>> half1 =['6', '8', 'K', 'Q'] 
>>> half2 = ['2', 'A', '5', '10']
>>> shuffled_deck = ['6', '2', 'A', '8', '5', 'K', 'Q', '10']
>>> is_single_riffle(half1, half2, shuffled_deck)
True
 '''

def is_single_riffle(half1, half2, shuffled_deck,
                    half1_indx=0, half2_indx=0, deck_indx=0):

    if deck_indx == len(shuffled_deck):
        return True

    if half1_indx < len(half1) and shuffled_deck[deck_indx] == half1[half1_indx]:
        half1_indx += 1
    elif half2_indx < len(half2) and shuffled_deck[deck_indx] == half2[half2_indx]:
        half2_indx += 1
    else:
        return False
    deck_indx  += 1



    return is_single_riffle(half1, half2, shuffled_deck,
                    half1_indx, half2_indx, deck_indx)


         




if __name__ ==  '__main__':
    import doctest

    if doctest.testmod().failed == 0:
        print('\n***TESTS PASSED***\n')
