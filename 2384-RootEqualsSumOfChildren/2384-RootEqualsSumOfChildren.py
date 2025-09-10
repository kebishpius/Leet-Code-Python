# Last updated: 9/10/2025, 12:55:27 AM
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def checkTree(self, root):
        if root.left.val + root.right.val == root.val:
            return True
        else:
            return False