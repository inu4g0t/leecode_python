# https://oj.leetcode.com/problems/remove-element/
# Given an array and a value, remove all instances of that value in place and return the new length.

# The order of elements can be changed. It doesn't matter what you leave beyond the new length.

class Solution:
    # @param    A       a list of integers
    # @param    elem    an integer, value need to be removed
    # @return an integer
    def removeElement(self, A, elem):
        if not A:
            return 0
        i = 0
        to_rm = list()
        while i < len(A):
            if A[i] == elem:
                to_rm.append(i)
            i = i + 1
        while not not to_rm:
            del A[to_rm.pop()]
        return len(A)
