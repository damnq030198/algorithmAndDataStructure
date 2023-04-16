# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None:
            return None
        p = root
        stack = []
        result = []
        while p :
            stack.append(p)
            p = p.left
        while len(stack)>0:
            t = stack.pop()
            result.append(t)
            t = t.right
            while t!=None:
                stack.append(t)
                t = t.left
        r = [i.val for i in result]
        
        return r