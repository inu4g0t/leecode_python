# https://oj.leetcode.com/problems/plus-one/

# Given a non-negative number represented as an array of digits, plus one to the number.

# The digits are stored such that the most significant digit is at the head of the list.

class Solution:
    # @param digits, a list of integer digits
    # @return a list of integer digits
    def plusOne(self, digits):
        if not digits:
            return
        i = len(digits)-1
        while i >= 0:
            if digits[i] == 9:
                digits[i] = 0
                i = i - 1 
                continue
            digits[i] = digits[i] + 1
            return digits 
        r = list()
        r.append(1)
        r.extend(digits)
        return r
