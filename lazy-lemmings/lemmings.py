"""Lazy lemmings.

Find the farthest any single lemming needs to travel for food.

    >>> furthest(3, [0, 1, 2])
    0

    >>> furthest(3, [2])
    2

    >>> furthest(3, [0])
    2

    >>> furthest(6, [2, 4])
    2

    >>> furthest(7, [0, 6])
    3

    >>> furthest_optimized(7, [0, 6])
    3

    >>> furthest_optimized(3, [0, 1, 2])
    0

    >>> furthest_optimized(3, [2])
    2

    
    >>> furthest_optimized(6, [2, 4])
    2
"""


def furthest(num_holes, cafes):
    """Find longest distance between a hole and a cafe.
    O(nxm) solution"""

  
    local_routes = []
    routes = []
    for i in range(num_holes):
        for j in cafes:
            local_routes.append(abs(i-j))
        routes.append(min(local_routes))
        local_routes = []
        
    print(max(routes))


def furthest_optimized(num_holes, cafes):
    '''O(n) solution'''
 
    left = 0
    max_route = 0 

    if cafes[0] != 0:
        max_route = cafes[0]
    if cafes[-1] != num_holes - 1 and max_route < num_holes - 1 - cafes[-1]:
        max_route = num_holes - 1 - cafes[-1]

    i = 0
       
    while i < len(cafes):
        route = int((cafes[i] - left)/2)
        if max_route < route:
            max_route = route
        left =cafes[i]
        i += 1
    
     
    print (max_route)

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED; GREAT JOB!\n")
