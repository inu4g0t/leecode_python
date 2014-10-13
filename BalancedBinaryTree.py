# https://oj.leetcode.com/problems/balanced-binary-tree/

# Given a binary tree, determine if it is height-balanced.

# For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None



class Solution:
    
    def isBalancedNum(self, root):
        if not root:
            return 0
# https://oj.leetcode.com/problems/balanced-binary-tree/

# Given a binary tree, determine if it is height-balanced.

# For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None



class Solution:
    
    def isBalancedNum(self, root):
        if not root:
            return 0
        l1 = self.isBalancedNum(root.left)
        if l1 == -1:
            return -1
        l2 = self.isBalancedNum(root.right)
        if l2 == -1:
            return -1
        if l1 == l2:
            return l1 + 1
        if l1 > l2:
            tmp = l1
            l1 = l2
            l2 = l1
        if l2 - l1 > 1:
            return -1
        return l1 + 1
    
    # @param root, a tree node
    # @return a boolean
    def isBalanced(self, root):
        if self.isBalancedNum(root) == -1:
            return False
        return True
        # https://oj.leetcode.com/problems/balanced-binary-tree/

# Given a binary tree, determine if it is height-balanced.

# For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None



class Solution:
    
    def isBalancedNum(self, root):
        if not root:
            return 0
        l1 = self.isBalancedNum(root.left)
        if l1 == -1:
            return -1
        l2 = self.isBalancedNum(root.right)
        if l2 == -1:
            return -1
        if l1 == l2:
            return l1 + 1
        if l1 > l2:
            tmp = l1
            l1 = l2
            l2 = l1
        if l2 - l1 > 1:
            return -1
        return l1 + 1
    
    # @param root, a tree node
    # @return a boolean
    def isBalanced(self, root):
        if self.isBalancedNum(root) == -1:
            return False
        return True
        # https://oj.leetcode.com/problems/balanced-binary-tree/

# Given a binary tree, determine if it is height-balanced.

# For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None



class Solution:
    
    def isBalancedNum(self, root):
        if not root:
            return 0
        l1 = self.isBalancedNum(root.left)
        if l1 == -1:
            return -1
        l2 = self.isBalancedNum(root.right)
        if l2 == -1:
            return -1
        if l1 == l2:
            return l1 + 1
        if l1 > l2:
            tmp = l1
            l1 = l2
            l2 = l1
        if l2 - l1 > 1:
            return -1
        return l1 + 1
    
    # @param root, a tree node
    # @return a boolean
    def isBalanced(self, root):
        if self.isBalancedNum(root) == -1:
            return False
        return True
                l1 = self.isBalancedNum(root.left)
        print(l1)
        if l1 == -1:
            return -1
        l2 = self.isBalancedNum(root.right)
        print(l2)
        if l2 == -1:
            return -1
        if l1 == l2:
            return l1 + 1
        if l1 > l2:
            tmp = l1
            l1 = l2
            l2 = tmp
        if l2 - l1 > 1:
            return -1
        return l2 + 1
    
    # @param root, a tree node
    # @return a boolean
    def isBalanced(self, root):
        if self.isBalancedNum(root) == -1:
            return False
        return True
        
