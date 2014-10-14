# https://oj.leetcode.com/problems/pascals-triangle/

# Given numRows, generate the first numRows of Pascal's triangle.

# For example, given numRows = 5,
# Return

# [
#      [1],
#     [1,1],
#    [1,2,1],
#   [1,3,3,1],
#  [1,4,6,4,1]
# ]


class Solution:
    # @return a list of lists of integers
    def generate(self, numRows):
        r = list()
        if numRows <= 0:
            return r
        cur = list()
        cur.append(1)
        r.append(cur)
        last = cur
        i = 1
        while i < numRows:
            cur = list()
            cur.append(1)
            inner_i = 0
            while inner_i < i-1:
                cur.append(last[inner_i] + last[inner_i + 1] )
                inner_i = inner_i + 1
            cur.append(1)
            r.append(cur)
            last = cur
            i = i + 1
        return r
