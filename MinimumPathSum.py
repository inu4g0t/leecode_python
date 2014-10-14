# https://oj.leetcode.com/problems/minimum-path-sum/

# Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

# Note: You can only move either down or right at any point in time.

class Solution:
    # @param grid, a list of lists of integers
    # @return an integer
    def minPathSum(self, grid):
        if not grid:
            return 0
        mp = list()
        cur = list()
        if not not grid[0]:
            cur.append(grid[0][0])
        j = 1
        while j < len(grid[0]):
            cur.append(cur[j-1] + grid[0][j])
            j = j + 1
        mp.append(cur)
        i = 1
        while i < len(grid):
            cur = list()
            cur.append(mp[i-1][0]+grid[i][0])
            j = 1
            while j < len(grid[i]):
                cur.append(min([mp[i-1][j], cur[j-1]]) + grid[i][j])
                j = j + 1
            mp.append(cur)
            i = i + 1
        return mp[len(grid)-1][len(grid[len(grid)-1])-1]

ip = list()
ip.append([1,2])
ip.append([5,6])
ip.append([1,1])
s = Solution()
print(s.minPathSum(ip))
