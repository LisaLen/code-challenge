"""Given a list of words, return the word with the most anagrams.

For a list of ['act', 'cat', 'bill']:
- 'act' and 'cat' are anagrams, so they both have 2 matching words.
- 'bill' has no anagrams, os it has one matching word (itself).

Given that 'act' is the first instance of the most-anagrammed word,
we return that.

    >>> find_most_anagrams_from_wordlist(['act', 'cat', 'bill'])
    'act'

Let's use a file of words where each line is a word:
    >>> import os, sys
    >>> all_words = [w.strip() for w in open(os.path.join(sys.path[0],'words.txt'))]
    >>> find_most_anagrams_from_wordlist(all_words)
    'angor'

"""
def make_anagram_dict(wordlist):

    out = {}
    for w in wordlist:
        sorted_word = ''.join(sorted(w))
        out.setdefault(sorted_word, []).append(w)
      
    return out



def find_most_anagrams_from_wordlist(wordlist):
    """Given list of words, return the word with the most anagrams."""
    anagram_dict = make_anagram_dict(wordlist)

    hightest_anagram = 0
    anagram_word = None

    for w in wordlist:
        sorted_word = ''.join(sorted(w))
        if len(anagram_dict[sorted_word]) > hightest_anagram:
            hightest_anagram = len(anagram_dict[sorted_word])
            anagram_word = w

    return anagram_word
    


if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. YAY!\n")
