'''You've built an inflight entertainment system with on-demand movie streaming.

Users on longer flights like to start a second movie right when their first one
 ends, but they complain that the plane usually lands before they can see the
  ending. So you're building a feature for choosing two movies whose total 
  runtimes will equal the exact flight length.

Write a function that takes an integer flight_length (in minutes) and a list
 of integers movie_lengths (in minutes) and returns a boolean indicating whether
 there are two numbers in movie_lengths whose sum equals flight_length.

When building your function:

Assume your users will watch exactly two movies
Don't make your users watch the same movie twice
Optimize for runtime over memory

>>> n = 100
>>> can_two_movies_fill_flight(100, [20, 30, 40, 70])
True
>>> can_two_movies_fill_flight(100, [30,40,50])
False
'''
def can_two_movies_fill_flight(flight_length, movie_lengths):

    movies_set = set(movie_lengths)
    seen = set()

    for m in movies_set:
        seen.add(m)
        second_movie = flight_length - m 
        if second_movie in (movies_set - seen):
            return True
        
    return False

if __name__ == '__main__':
    import doctest

    if doctest.testmod().failed == 0:
        print('\n*** TEST PASSES***\n')