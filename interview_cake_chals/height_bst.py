class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    def getHeight(self,root):
        #Write your code here
        # if not root:
        #     return -1
        if root.left:
            hleft =1 + self.getHeight(root.left)
        else:
            hleft = 0
        if root.right:
            hright = 1+ self.getHeight(root.right)
        else:
            hright = 0
        print(root.data, hleft, hright)
        return max(hleft, hright)

T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    
    root=myTree.insert(root,data)
   


height=myTree.getHeight(root)
print(height)    