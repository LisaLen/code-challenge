'''Write a function to see if a binary tree ↴ is "superbalanced" 
(a new tree property we just made up).

A tree is "superbalanced" if the difference between the depths of any two leaf 
nodes ↴ is no greater than one.

  >>> t4 = BinaryTreeNode(4)
  >>> t2 = t4.insert_left(2)
  >>> t6 = t4.insert_right(6)
  >>> t1 = t2.insert_left(1)
  >>> t3 = t2.insert_right(3)
  >>> t5 = t6.insert_left(5)
  >>> t7 = t6.insert_right(7)
 
  >>> t4.is_superbalanced()
  True

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
    
    

    def is_superbalanced(self):
        if not self: 
            return True

        def hight_tree(node):
            if not node:
                return 0
            
            hight_left = hight_tree(node.left)
            hight_right = hight_tree(node.right)
            hight = max(hight_left, hight_right) + 1

            return hight

        if abs(hight_tree(self.left) - hight_tree(self.right)) <= 1:
            return True
        return False




if __name__=='__main__':
    import doctest

    if doctest.testmod().failed == 0:
        print('\n***PASSED***\n')