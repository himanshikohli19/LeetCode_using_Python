'''
144. Binary Tree Preorder Traversal

Given the root of a binary tree,
return the preorder traversal of its nodes' values.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        list1=[]
        def preorder(root):
            if root==None:
                return
            list1.append(root.val)
            if (root.left):
                preorder(root.left)
            if (root.right):
                preorder(root.right)
        preorder(root)
        return list1
