# https://oj.leetcode.com/problems/binary-tree-inorder-traversal/

# Given a binary tree, return the inorder traversal of its nodes' values.

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def inorderTraversal(self, root):
        rl = list()
        if root is None:
            return rl
        stack = list()
        cur = root
        while not not cur or not not stack:
            while not not cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            rl.append(cur.val)
            cur = cur.right
        return rl
