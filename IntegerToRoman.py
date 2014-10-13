# https://oj.leetcode.com/problems/integer-to-roman/

# Given an integer, convert it to a roman numeral.

# Input is guaranteed to be within the range from 1 to 3999.

class Solution:
    # @return a string
    def intToRoman(self, num):
        s = ''
        if num == 0:
            return s
        l1 = list()
        l1.append('I')
        l1.append('X')
        l1.append('C')
        l1.append('M')
        l2 = list()
        l2.append('V')
        l2.append('L')
        l2.append('D')
        if num >= 1000:
            s = s + 'M'*(num // 1000)
            num = num % 1000
        i = 2
        while i >= 0:
            if num == 0:
                break
            d= num // 10**i
            num = num % 10**i
            if d == 9:
                s = s + l1[i]+l1[i+1] 
            elif d == 4:
                s = s + l1[i]+l2[i]
            else:
                if d >=5:
                    s = s + l2[i]
                    d = d - 5
                s = s + l1[i]*d
            i = i - 1
        return s
            
