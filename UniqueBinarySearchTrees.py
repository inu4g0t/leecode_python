# https://oj.leetcode.com/problems/unique-binary-search-trees/

# Given n, how many structurally unique BST's (binary search trees) that store values 1...n?

class Solution:
    # @return an integer
    def numTrees(self, n):
        l = list()
        l.append(1)
        l.append(1)
        l.append(2)
        index = 3
        while index <= n:
            inner_i = 0
            cur = 0
            while inner_i < index:
                cur = cur + l[inner_i] * l[index-inner_i-1]
                inner_i = inner_i + 1
            l.append(cur)
            index = index + 1
        return l[n]
