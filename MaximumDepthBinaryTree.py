# https://oj.leetcode.com/problems/maximum-depth-of-binary-tree/

# Given a binary tree, find its maximum depth.

# The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.


# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def maxDepth(self, root):   
        max_d = 0
        cur_d = 0
        if not (root is None):
            stack = list()
            stack_n = list()
            cur_n = root
            while cur_n is not None or not not stack:
                while not not cur_n:
                    stack.append(cur_n)
                    cur_d = cur_d + 1
                    stack_n.append(cur_d)
                    cur_n = cur_n.left
                if cur_d > max_d:
                    max_d = cur_d
                cur_n = stack.pop()
                cur_d = stack_n.pop()
                cur_n = cur_n.right
        return max_d
            
            
                
        
