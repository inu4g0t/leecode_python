# https://oj.leetcode.com/problems/symmetric-tree/

# Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    def isSymmetric(self, root):
        if not root:
            return True
        stack_p = list()
        stack_q = list()
        cur_p = root
        cur_q = root
        while not not cur_p or not not stack_p:
            while not not cur_p:
                if not cur_q:
                    return False
                if cur_p.val != cur_q.val:
                    return False
                stack_p.append(cur_p)
                stack_q.append(cur_q)
                cur_p = cur_p.left
                cur_q = cur_q.right
            if not not cur_q:
                return False
            cur_p = stack_p.pop()
            cur_q = stack_q.pop()
            cur_p = cur_p.right
            cur_q = cur_q.left
        if not not cur_q or not not stack_q:
            return False
        return True
