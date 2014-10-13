# https://oj.leetcode.com/problems/search-insert-position/

# Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
# 
# You may assume no duplicates in the array.
# 
# Here are few examples.
# [1,3,5,6], 5 → 2
# [1,3,5,6], 2 → 1
# [1,3,5,6], 7 → 4
# [1,3,5,6], 0 → 0


class Solution:
    # @param A, a list of integers
    # @param target, an integer to be inserted
    # @return integer
    def searchInsert(self, A, target):
        if not A:
            return 0
        start = 0
        if A[start] >= target:
            return start
        end = len(A)-1
        if A[end] == target:
            return end
        if A[end] < target:
            return end+1
        while end - start > 1:
            mid = (start + end) // 2
            if A[mid] == target:
                return mid
            if A[mid] > target:
                end = mid
            else:
                start = mid
        return end
        
