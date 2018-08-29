"""Given a string, return True if it is a pangram, False otherwise.

For example::

    >>> is_pangram("The quick brown fox jumps over the lazy dog!")
    True
    
    >>> is_pangram("I love cats, but not mice")
    False
"""


def is_pangram(sentence):
    """Given a string, return True if it is a pangram, False otherwise."""
    string = set()
    for letter in sentence.lower():
        if letter.isalpha() and letter not in string:
            string.add(letter)
    if len(string) == 26:
        return True
    return False


if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. YAY!\n")
