# https://oj.leetcode.com/problems/climbing-stairs/

# You are climbing a stair case. It takes n steps to reach to the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

class Solution:
    # @param n, an integer
    # @return an integer
    def climbStairs(self, n):
        f = list()
        f.append(1)
        f.append(1)
        index = 2
        while index <= n:
            f.append(f[index-1] + f[index-2])
            index = index + 1
        return f[n]
        
