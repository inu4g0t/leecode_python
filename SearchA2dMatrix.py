# https://oj.leetcode.com/problems/search-a-2d-matrix/

# Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

# Integers in each row are sorted from left to right.
# The first integer of each row is greater than the last integer of the previous row.
# For example,

# Consider the following matrix:

# [
#   [1,   3,  5,  7],
#   [10, 11, 16, 20],
#   [23, 30, 34, 50]
# ]
# Given target = 3, return true.

class Solution:
    # @param matrix, a list of lists of integers
    # @param target, an integer
    # @return a boolean
    def searchMatrix(self, matrix, target):
        if not matrix or not matrix[0]:
            return False
        m = len(matrix)
        n = len(matrix[0])
        s = 0
        e = m * n - 1
        mid = (s + e) // 2
        while s != mid and e != mid:
            if matrix[mid // n][mid % n] == target:
                return True
            elif matrix[mid // n][mid % n] < target:
                s = mid
            else:
                e = mid
            mid = (s + e) // 2
        if matrix[mid // n][mid % n] == target:
            return True
        if matrix[e // n][e % n] == target:
            return True
        return False
