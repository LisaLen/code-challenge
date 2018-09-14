'''
You created a game that is more popular than Angry Birds.

Each round, players receive a score between 0 and 100, which you use to rank 
them from highest to lowest. So far you're using an algorithm that sorts in 
O(n\lg{n})O(nlgn) time, but players are complaining that their rankings aren't 
updated fast enough. You need a faster sorting algorithm.

Write a function that takes:

a list of unsorted_scores
the highest_possible_score in the game
and returns a sorted list of scores in less than O(n\lg{n})O(nlgn) time.

For example:

>>> unsorted_scores = [37, 89, 90, 90, 41, 65, 65, 65, 91, 53]
>>> HIGHEST_POSSIBLE_SCORE = 100


>>> sort_scores(unsorted_scores, HIGHEST_POSSIBLE_SCORE)
[91, 90, 90, 89, 65, 65, 65, 53, 41, 37]

'''

def sort_scores(unsorted_scores, highest):

    scores_dict = {}
    for score in unsorted_scores:
        scores_dict[score] = scores_dict.setdefault(score, 0) + 1

    
    sorted_lst = []

    for i in range(highest, -1, -1):
        if i in scores_dict:
            for j in range(scores_dict[i]):
                sorted_lst.append(i)

    return sorted_lst






if __name__ == '__main__':
    import doctest

    if doctest.testmod().failed == 0:
        print('\n***TEST PASSED***\n')