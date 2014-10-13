# https://oj.leetcode.com/problems/n-queens-ii/

# Follow up for N-Queens problem.

# Now, instead outputting board configurations, return the total number of distinct solutions.

class Solution:
    def totalNQueensRec(self, qs_pos, n):
        cur = len(qs_pos)
        if cur == n:
            return 1
        index = 0
        sum = 0
        while index < n:
            i = 0
            if_valid = True
            while i < cur:
                if  qs_pos[i] == index or qs_pos[i] - index == i - cur or qs_pos[i]\
 - index == cur - i:
                    if_valid = False
                    break
                i =i + 1
            if if_valid:
                qs_pos.append(index)
                sum = sum + Solution.totalNQueensRec(self,qs_pos,n)
                qs_pos.pop()
            index = index + 1
        #print(sum)                                                                 
        return sum
    
    # @return an integer
    def totalNQueens(self, n):
        if n == 1:
            return 1
        qs_pos = list()
        return Solution.totalNQueensRec(self, qs_pos, n)
