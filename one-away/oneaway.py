"""Given two strings, are they, at most, one edit away?

    >>> one_away("make", "make")
    True

    >>> one_away("make", "fake")
    True

    >>> one_away("task", "take")
    False

    >>> one_away("ask" ,"asks")
    True

    >>> one_away("asks", "ask")
    True

    >>> one_away("act", "tact")
    True

    >>> one_away("fat", "fact")
    True

    >>> one_away("yes", "no")
    False


"""

def one_away(w1, w2):
    """Given two strings, are they, at most, one edit away?"""
    
    if abs(len(w1) - len(w2)) > 1:
        return False

    count_diff = 0

    i = j = 0
    len_diff = len(w1) - len(w2)

    while i < len(w1) and i < len(w2):
        if w1[i] != w2[j]:
            count_diff += 1
            if len_diff == 0:
                i += 1
                j += 1
            elif len_diff < 0:
                j += 1
            else: 
                i += 1
            continue

        i += 1
        j += 1

    
    return count_diff < 2










if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED; NICE JOB! ***\n")
