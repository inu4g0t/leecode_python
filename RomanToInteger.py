# https://oj.leetcode.com/problems/roman-to-integer/

# Given a roman numeral, convert it to an integer.

# Input is guaranteed to be within the range from 1 to 3999.

class Solution:
    # @return an integer
    def romanToInt(self, s):
        if not s:
            return 0
        sl = list(s)
        roman_dict = dict()
        roman_dict['I'] = 1
        roman_dict['V'] = 5
        roman_dict['X'] = 10
        roman_dict['L'] = 50
        roman_dict['C'] = 100
        roman_dict['D'] = 500
        roman_dict['M'] = 1000
        r = 0
        index = 0
        l = len(s)
        while index < l:
            if ( index + 1 < l ):
                if roman_dict[sl[index]] < roman_dict[sl[index+1]]:
                    r = r + roman_dict[sl[index+1]] - roman_dict[sl[index]]
                    index = index + 2
                else:
                    r = r + roman_dict[sl[index]]
                    index = index + 1
            else:
                r = r + roman_dict[sl[index]]
                break
        return r
