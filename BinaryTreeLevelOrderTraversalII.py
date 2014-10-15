# https://oj.leetcode.com/problems/binary-tree-level-order-traversal-ii/

# Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

# For example:
# Given binary tree {3,9,20,#,#,15,7},
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its bottom-up level order traversal as:
# [
#   [15,7],
#   [9,20],
#   [3]
# ]

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def levelOrderBottom(self, root):
        r = list()
        if not root:
            return r
        cur = list()
        cur.append(root)
        while not not cur and len(cur) != 0:
            prev = cur
            curVal = list()
            cur = list()
            for n in prev:
                curVal.append(n.val)
                if not not n.left:
                    cur.append(n.left)
                if not not n.right:
                    cur.append(n.right)
            r.insert(0,curVal)
        return r
