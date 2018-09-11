'''Write a function reverse_words() that takes a message as a list of characters
 and reverses the order of the words in place.

    >>> message = [ 'c', 'a', 'k', 'e', ' ', 'p', 'o', 'u', 'n', 'd', ' ', 's', 't', 'e', 'a', 'l' ]

    >>> rev = reverse_words(message)
    >>> rev
    ['s', 't', 'e', 'a', 'l', ' ', 'p', 'o', 'u', 'n', 'd', ' ', 'c', 'a', 'k', 'e']
    >>> rev is message
    True


 '''
def reverse_characters(message):
    '''reverse list in-place'''
    len_msg = len(message)
    pivot = len_msg // 2


    for i in range(pivot):
        message[i], message[len_msg-1-i] = message[len_msg-1-i], message[i]
    return message




def reverse_words(message):
    '''reverse string of words in place'''

    reverse_characters(message)

    start_word = 0
    for i in range(len(message)):
        
        if message[i] == ' ':
            message[start_word:i] = reverse_characters(message[start_word:i])
            start_word = i + 1
        elif i == len(message) - 1:
            message[start_word:] = reverse_characters(message[start_word:])


    


    return message
   
        




if __name__ == '__main__':
    import doctest

    if doctest.testmod().failed == 0:
        print('\n***TESTS PASSED***\n')