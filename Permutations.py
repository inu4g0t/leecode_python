# https://oj.leetcode.com/problems/permutations/

# Given a collection of numbers, return all possible permutations.

# For example,
# [1,2,3] have the following permutations:
# [1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], and [3,2,1].

class Solution:
    
    def permuteRec(self, num, pos):
        if not num:
            return None
        r = list()
        cur = list()
        ln = len(num)
        if pos == ln - 1:
            cur.append(num[pos])
            r.append(cur)
            return r
        i = pos
        while i < ln:
            tmp = num[i]
            num[i] = num[pos]
            num[pos] = tmp
            for re in self.permuteRec(num, pos + 1):
                re.insert(0, tmp)
                r.append(re)
            tmp = num[i]
            num[i] = num[pos]
            num[pos] = tmp
            i = i + 1
        return r
    
    # @param num, a list of integer
    # @return a list of lists of integers
    def permute(self, num):
        if not num:
            return
        return self.permuteRec(num, 0)
