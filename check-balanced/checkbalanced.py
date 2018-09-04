"""Is the tree at this node balanced?

To make this a bit more readable, let's alias our class name:

    >>> N = BinaryNode

For a tree of 1 item:

    >>> tree1 = N(1)
    >>> tree1.is_balanced()
    True

For a tree of 2 items:

  1
 /
2

    >>> tree2 = N(1,
    ...           N(2))
    >>> tree2.is_balanced()
    True

Three:

  1
 / \
2   3

    >>> tree3 = N(1,
    ...           N(2), N(3))
    >>> tree3.is_balanced()
    True

Four:

     1
    / \
   2   4
  /
 3

    >>> tree4 = N(1,
    ...           N(2,
    ...             N(3)),
    ...           N(4))
    >>> tree4.is_balanced()
    True

Five:

     1
   /---\
  2     5
 / \
3   4

    >>> tree5 = N(1,
    ...           N(2,
    ...             N(3), N(4)),
    ...           N(5))
    >>> tree5.is_balanced()
    True

Imbalanced Four:

    1
   /
  2
 / \
3   4

    >>> tree4i = N(1,
    ...            N(2,
    ...              N(3), N(4)))
    >>> tree4i.is_balanced()
    False

Imbalanced Six:

    1
   / \
  2   6
 / \
3   4
   /
  5

    >>> tree6i = N(1,
    ...         N(2,
    ...       N(3), N(4,
    ...           N(5))),
    ...                   N(6))
    >>> tree6i.is_balanced()
    False

    >>> tree7i = N(1,
    ...         N(2,
    ...       N(3), N(4,
    ...           N(5))),
    ...                   N(6, N(7)))
    >>> tree7i.is_balanced()
    False

    >>> tree8i = N(1, N(2, N(3, N(4)), N(5)), 
    ...               N(6, N(7, N(8)), N(9, N(10, N(11)), N(12)))
    ...            )
    >>> tree8i.is_balanced()
    False

"""


class BinaryNode(object):
    """Node in a binary tree."""

    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def is_balanced(self):
        """Is the tree at this node balanced?"""
        path = bounds(self)
        return path[1] - path[0] <= 1

def bounds(node):
    if node:
      left  = bounds(node.left)
      right = bounds(node.right)
      shortest = min([left[0], right[0]]) + 1
      longest  = max([left[1], right[1]]) + 1 
      return (shortest, longest)
    return (0, 0)

    # def is_balanced(self):
    #       """Is the tree at this node balanced?"""

    #       # START SOLUTION

    #       def _num_descendants(node):
    #           """Returns number of descendants or None if already imbalanced."""

    #           if not node:
    #               # Our base case: we're not a real node (child of a leaf)
    #               return 0

    #           # Get descendants on left; if "None", already imbalanced---bail out
    #           left = _num_descendants(node.left)

    #           if left is None:
    #               return None

    #           # Get descendants on right; if "None", already imbalanced---bail out
    #           right = _num_descendants(node.right)

    #           if right is None:
    #               return None

    #           if abs(left - right) > 1:
    #               # Heights vary by more than 1 -- imbalanced!
    #               return None

    #           # Height of this node is height of our deepest descendant + ourselves
    #           return max(left, right) + 1

    #       return _num_descendants(self) is not None

if __name__ == '__main__':
    import doctest

    if doctest.testmod().failed == 0:
        print("\n*** ALL TEST PASSED! GO GO GO!\n")
