# 118. Pascal's Triangle
# https://leetcode.com/problems/pascals-triangle/

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        if numRow s= =1:
            return [[1]] l=[[1],[1, 1]]
        if numRows==2:
            return l
        a=[1,1]
        for i in range(numRows-2):
            b=[1]
            for j in range(len(a)-1):
                b.append(a[j]+a[j+1])

            b.append(1)
            a=b
            l.append(b)
        return l



