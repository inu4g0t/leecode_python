# https://oj.leetcode.com/problems/rotate-image/

# You are given an n x n 2D matrix representing an image.

# Rotate the image by 90 degrees (clockwise).

# Follow up:
# Could you do this in-place?

class Solution:
    # @param matrix, a list of lists of integers
    # @return a list of lists of integers
    def rotate(self, matrix):
        n  = len(matrix)
        i = 0
        while i < n // 2:
            j = i
            while j < n - i - 1:
                tmp1 = matrix[j][n-i-1]
                matrix[j][n-i-1] = matrix[i][j]
                tmp2 = matrix[n-i-1][n-j-1]
                matrix[n-i-1][n-j-1] = tmp1
                tmp1 = matrix[n-j-1][i]
                matrix[n-j-1][i] = tmp2
                matrix[i][j] = tmp1
                j = j + 1
            i = i + 1
        return matrix
