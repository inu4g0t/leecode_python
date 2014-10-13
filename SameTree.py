# https://oj.leetcode.com/problems/same-tree/

# Given two binary trees, write a function to check if they are equal or not.

# Two binary trees are considered equal if they are structurally identical and the nodes have the same value.


# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param p, a tree node
    # @param q, a tree node
    # @return a boolean
    def isSameTree(self, p, q):
        if p is q:
            return True
        if p is None or q is None:
            return False
        stack_p = list()
        stack_q = list()
        cur_p = p
        cur_q = q
        while not not cur_p or not not stack_p:
            while not not cur_p:
                if cur_p is cur_q:
                    cur_p = None
                    cur_q = None
                    break
                if not cur_q:
                    return False
                if cur_p.val != cur_q.val:
                    return False
                stack_p.append(cur_p)
                stack_q.append(cur_q)
                cur_p = cur_p.left
                cur_q = cur_q.left
            if not not cur_q:
                return False
            cur_p = stack_p.pop()
            cur_q = stack_q.pop()
            cur_p = cur_p.right
            cur_q = cur_q.right
        if not not cur_q or not not stack_q:
            return False
        return True
                
        
