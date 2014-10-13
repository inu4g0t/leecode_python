# https://oj.leetcode.com/problems/maximum-subarray/

# Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

# For example, given the array [−2,1,−3,4,−1,2,1,−5,4],
# the contiguous subarray [4,−1,2,1] has the largest sum = 6.


class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxSubArray(self, A):
        if not A:
            return 0
        ans=A[0]
        sum=0
        i = 0
        while i < len(A):
            sum = sum + A[i]
            if ans < sum:
                ans=sum
            if sum<0:
                sum=0
            i = i + 1
        return ans
