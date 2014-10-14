# https://oj.leetcode.com/problems/generate-parentheses/

# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

# For example, given n = 3, a solution set is:

# "((()))", "(()())", "(())()", "()(())", "()()()"

class Solution:
    # @param an integer
    # @return a list of string
    def generateParenthesis(self, n):
        r = list()
        if n < 1 != 0:
            return r
        cur = list()
        cur.append('()')
        r.append(cur)
        i = 1
        while i < n:
            cur = list()
            for s in r[i-1]:
                cur.append('()'+s)
            inner_i = 1
            while inner_i <= i:
                tmp = '('
                for s1 in r[inner_i-1]:
                    tmp1 = tmp + s1 + ')'
                    if inner_i == i:
                        cur.append(tmp1)
                    else:
                        for s2 in r[i - inner_i - 1]:
                            tmp2 = tmp1 + s2
                            cur.append(s2)
                inner_i = inner_i + 1
            r.append(cur)
            i = i + 1
        return r[n-1]

a = Solution()
re = a.generateParenthesis(4)
for s in re:
    print(s)
