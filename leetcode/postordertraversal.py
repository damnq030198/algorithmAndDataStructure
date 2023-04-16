# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack =[root]
        ls = []
        if root == None:
            return None
        while len(stack) !=0:
            tmp = stack[len(stack)-1]
            if tmp.right == None and tmp.left == None:
                root = stack.pop()
                ls.append(root.val)
            if tmp.right:
                stack.append(tmp.right)
                tmp.right = None
                
            if tmp.left:
                stack.append(tmp.left)
                tmp.left = None
                
        return ls