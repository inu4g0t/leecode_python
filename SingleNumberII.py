# https://oj.leetcode.com/problems/single-number-ii/

# Given an array of integers, every element appears three times except for one. Find that single one.

# Note:
# Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        ones = 0
        twos = 0
        threes = 0
        for a in A:
            twos = twos | ones & a
            ones = ones ^ a
            threes = ones & twos
            ones = ones & ~threes
            twos = twos & ~threes
        return ones
