"""Convert a hexadecimal string, like '1A', into it's decimal equivalent.

    >>> hex_convert('6')
    6

    >>> hex_convert('10')
    16

    >>> hex_convert('FF')
    255

    >>> hex_convert('FFFF')
    65535
"""

letters = {'A': 10,'B':11,'C':12,'D':13,'E':14,'F':15}

def hex_convert(hex_in):
    """Convert a hexadecimal string, like '1A', into it's decimal equivalent."""
    out = 0
    if len(hex_in) == 1:
        if hex_in in '0123456789':
            return int(hex_in)
        elif hex_in in 'ABCDEF':
            return letters[hex_in]
        else:
            raise ValueError

    for i in range(len(hex_in)):
        indx = len(hex_in) - 1 - i
        if hex_in[indx] in 'ABCDEF':
            val = letters[hex_in[indx]]
        else:
            val = int(hex_in[indx])
        
        out += val * 16 ** i
    print(out)


if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASS. YOU'RE TERRIFIC!\n")
