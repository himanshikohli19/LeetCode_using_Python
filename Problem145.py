'''
145. Binary Tree Postorder Traversal

Given the root of a binary tree,
return the postorder traversal of its nodes' values.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        list1=[]
        def postorder(root):
            if root == None:
                return
            if root.left:
                postorder(root.left)
            if root.right:
                postorder(root.right)
            list1.append(root.val)
        postorder(root)
        return list1
        
