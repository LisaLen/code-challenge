'''Write a function to find the 2nd largest element in a binary search tree.

  >>> t4 = BinaryTreeNode(5)
  >>> t2 = t4.insert_left(3)
  >>> t6 = t4.insert_right(7)
  >>> t1 = t2.insert_left(1)
  >>> t3 = t2.insert_right(2)
  >>> t33 = t6.insert_left(6)
  >>> t34 = t6.insert_right(9)
  >>> t5 = t34.insert_left(8)
  >>> t7 = t34.insert_right(10)
  >>> find_second_max(t4)
  9
 
'''
class BinaryTreeNode(object):

    def __init__(self, value):
        self.value = value
        self.left  = None
        self.right = None

    def insert_left(self, value):
        self.left = BinaryTreeNode(value)
        return self.left

    def insert_right(self, value):
        self.right = BinaryTreeNode(value)
        return self.right

def find_second_max (node):
    
    if node.right and not node.right.right:
        return node.value
    return find_second_max(node.right)


if __name__=='__main__':
    import doctest

    if doctest.testmod().failed == 0:
        print('\n***PASSED***\n')