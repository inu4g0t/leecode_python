# https://oj.leetcode.com/problems/convert-sorted-array-to-binary-search-tree/

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param num, a list of integers
    # @return a tree node
    def sortedArrayToBST(self, num):
        if not num:
            return None
        if len(num) == 1:
            return TreeNode(num[0])
        mid = len(num) // 2
        r = TreeNode(num[mid])
        if mid != 0:
            r.left = self.sortedArrayToBST(num[0:mid])
        if mid != len(num) -1:
            r.right = self.sortedArrayToBST(num[mid +1:len(num)])
        return r
