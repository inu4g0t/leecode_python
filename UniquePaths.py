# https://oj.leetcode.com/problems/unique-paths/

# A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

# The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

# How many possible unique paths are there?

class Solution:
    # @return an integer
    def uniquePaths(self, m, n):
        
        # sum = C(m+n, m)
        
        m = m - 1
        n = n - 1
        if m == 0 or n == 0:
            return 1
        if m < n:
            tmp = m
            m = n
            n = tmp
        i = m + n
        sum = 1
        while i > m:
            sum = sum * i
            i = i - 1
        i = n
        while i > 0:
            sum = sum / i
            i = i - 1
        return sum
            
