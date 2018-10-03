'''Write a function to check that a binary tree ↴ is a valid binary search tree
  
  >>> t4 = BinaryTreeNode(10)
  >>> t2 = t4.insert_left(5)
  >>> t6 = t4.insert_right(13)
  >>> t1 = t2.insert_left(2)
  >>> t3 = t2.insert_right(6)
  >>> t33 = t3.insrt_left(3)
  >>> t33 = t3.insert_right(11)
  >>> t5 = t6.insert_left(12)
  >>> t7 = t6.insert_right(14)
  >>> is_bst(t4)
  False
  >>> t4 = BinaryTreeNode(4)
  >>> t2 = t4.insert_left(8)
  >>> t6 = t4.insert_right(6)
  >>> t1 = t2.insert_left(1)
  >>> t3 = t2.insert_right(3)
  >>> t5 = t6.insert_left(5)
  >>> t7 = t6.insert_right(7)
  >>> is_bst(t4)
  False


'''


class BinaryTreeNode(object):

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def insert_left(self, value):
        self.left = BinaryTreeNode(value)
        return self.left

    def insert_right(self, value):
        self.right = BinaryTreeNode(value)
        return self.right


def is_bst(node, max_val = float('+inf'), min_val = float('-inf')):
    if not node:
        return True
    print(node.val, max_val, min_val)
    if node.val >= max_val or node.val < min_val:
        return False
    return is_bst(node.left, node.val, min_val) and is_bst(node.right, max_val, node.val)


if __name__=='__main__':
    import doctest

    if doctest.testmod().failed == 0:
        print('\n***PASSED***\n')