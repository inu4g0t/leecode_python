# https://oj.leetcode.com/problems/container-with-most-water/

# Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

# Note: You may not slant the container.

class Solution:
    # @return an integer
    def maxArea(self, height):
        if not height or len(height) == 1:
            return 0
        max = 0
        s = 0
        e = len(height) - 1
        while s != e:
            if height[s] < height[e]:
                cur = height[s] * (e - s)
                s = s + 1
            else:
                cur = height[e] * (e - s)
                e = e - 1
            if max < cur:
                max = cur
        return max
