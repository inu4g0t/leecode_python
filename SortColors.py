# https://oj.leetcode.com/problems/sort-colors/

# Given an array with n objects colored red, white or blue, sort them so that objects of the same color are adjacent, with the colors in the order red, white and blue.

# Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

# Note:
# You are not suppose to use the library's sort function for this problem.

# click to show follow up.

# Follow up:
# A rather straight forward solution is a two-pass algorithm using counting sort.
# First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's, then 1's and followed by 2's.

# Could you come up with an one-pass algorithm using only constant space?


class Solution:
    # @param A a list of integers
    # @return nothing, sort in place
    def sortColors(self, A):
        if not A:
            return
        l = [0,0,0]
        for a in A:
            l[a] = l[a] + 1
        c = 0
        i = 0
        while i < 3:
            index = 0
            while index < l[i]:
                A[c] = i
                index = index + 1
                c = c + 1
            i = i + 1
            
        
