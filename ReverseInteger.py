# https://oj.leetcode.com/problems/reverse-integer/

# Reverse digits of an integer.

# Example1: x = 123, return 321
# Example2: x = -123, return -321

class Solution:
    # @return an integer
    def reverse(self, x):
        if not x:
            return 0
        if x >-10 and x < 10:
            return x
        x_cs=list(str(x))
        x_cs.reverse()
        if x_cs[len(x_cs)-1] == '-':
            del x_cs[len(x_cs)-1]
            x_cs.insert(0,'-')
        return int(''.join(x_cs))
            
