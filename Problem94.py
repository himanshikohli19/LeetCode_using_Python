'''
94. Binary Tree Inorder Traversal

Given the root of a binary tree, return the inorder traversal
of its nodes' values.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        list1=[]
        def inorder(root):
            if root==None:
                return
            if (root.left):
                inorder(root.left)
            list1.append(root.val)
            if (root.right):
                inorder(root.right)
        inorder(root)
        return list1
