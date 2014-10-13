# https://oj.leetcode.com/problems/populating-next-right-pointers-in-each-node/

# Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

# Initially, all next pointers are set to NULL.

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree node
    # @return nothing
    def connect(self, root):
        if not root:
            return
        l = list()
        l.append(root)
        while not not l:
            ll = list()
            for n in l:
                if not not n.left:
                    n.left.next = n.right
                    ll.append(n.left)
                if not not n.right:
                    ll.append(n.right)
                    if not not n.next:
                        n.right.next = n.next.left
            l=ll
        
