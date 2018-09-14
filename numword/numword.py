"""Convert an integer number to the word representation.

We should handle zero:

    >>> num_word(0)
    'zero'

And numbers under a thousand:

    >>> num_word(2)
    'two'

    >>> num_word(-2)
    'negative two'

    >>> num_word(11)
    'eleven'

    >>> num_word(20)
    'twenty'

    >>> num_word(100)
    'one hundred'

    >>> num_word(121)
    'one hundred twenty one'

And numbers over a thousand:

    >>> num_word(1256)
    'one thousand two hundred fifty six'

    >>> num_word(100001)
    'one hundred thousand one'

    >>> num_word(1000000)
    'one million'

And all numbers ranging from -999,999,999,999 to 999,999,999,999 (you
can stop there):

    >>> num_word(-1234567890)  # doctest:+NORMALIZE_WHITESPACE
    'negative one billion two hundred thirty four million five hundred sixty seven thousand eight hundred ninety'

    >>> num_word(999999999999)  # doctest:+NORMALIZE_WHITESPACE
    'nine hundred ninety nine billion nine hundred ninety nine million nine hundred ninety nine thousand nine hundred ninety nine'

"""
ONES = ['','one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine',
        'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen',
        'seventeen', 'eighteen', 'nineteen']

TENS = ['', '', 'twenty', 'thirty', 'fourty', 'fifty', 'sixty', 'sevey', 'eighty', 'ninety']

THOUSANDS = ['', 'thousand ', 'million ', 'billion ']


def clusters(num):
    ''' for num in 1 - 999 ->text

    All numbers end with space, which will either be used or stripped off.

        >>> clusters(1)
        'one '

        >>> clusters(11)
        'eleven '

        >>> clusters(121)
        'one hundred twenty one '
    '''
    out = ''

    if num >=100:
        out += ONES[num // 100] + ' hundred '
        num %= 100
    if num >= 20:
        out += TENS[num // 10] + ' '
        num %= 10
    out += ONES[num] + ' '

    return out




def num_word(num):
    """Convert number  to word."""

    if num < 0:
        # call recursively, prepending with 'negative'
        return "negative " + num_word(abs(num))

    # Handle clusters of 3 digits (123,456,789 = chunks of 123 456 789)
    #
    # Order: ones->thousands->millions->billions. Cluster text goes at
    # end of out, so it appears in billion-million-thousand-ones order.

    out = ""
    cluster = 0  # 0=ones, 1=thousands, 2=millions, 3=billions

    while num > 0:
        cluster_val = num % 1000  # 1234 -> 234
        num //= 1000  # 1234 -> 1

        if cluster_val > 0:
            # Print only if >0 --  otherwise 1,000,000 would be
            # "1 million thousand" (since there are zero thousands)
            out = clusters(cluster_val) + THOUSANDS[cluster] + out

        cluster += 1

    return out.rstrip() or "zero"





















if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. GREAT JOB!\n")
