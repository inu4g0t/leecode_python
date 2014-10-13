# https://oj.leetcode.com/problems/remove-duplicates-from-sorted-array/

# Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.

# Do not allocate extra space for another array, you must do this in place with constant memory.

# For example,
# Given input array A = [1,1,2],

# Your function should return length = 2, and A is now [1,2].

class Solution:
    # @param a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        if not A:
            return 0
        i = 0
        cur = -1
        not_set = True
        prev = None
        while i < len(A):
            if not_set or prev != A[i]:
                prev = A[i]
                cur = cur + 1
                A[cur] = prev
                not_set = False
            i = i + 1
        return cur + 1
        
