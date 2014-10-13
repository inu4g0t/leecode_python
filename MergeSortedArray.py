# https://oj.leetcode.com/problems/merge-sorted-array/

# Given two sorted integer arrays A and B, merge B into A as one sorted array.

# Note:
# You may assume that A has enough space (size that is greater or equal to m + n) to hold additional elements from B. The number of elements initialized in A and B are m and n respectively.

class Solution:
    # @param A  a list of integers
    # @param m  an integer, length of A
    # @param B  a list of integers
    # @param n  an integer, length of B
    # @return nothing
    def merge(self, A, m, B, n):
        merged = list()
        cur_m = m-1
        cur_n = n-1
        cur_merged = m + n -1
        while cur_m >= 0 or cur_n >= 0 :
            if cur_m < 0:
                A[cur_merged] = B[cur_n]
                cur_n = cur_n - 1
                cur_merged = cur_merged -1
                continue
            if cur_n < 0:
                break
            if A[cur_m] > B[cur_n] :
                A[cur_merged] = A[cur_m]
                cur_merged = cur_merged -1
                cur_m = cur_m - 1
            else:
                A[cur_merged] = B[cur_n]
                cur_merged = cur_merged -1
                cur_n = cur_n - 1
