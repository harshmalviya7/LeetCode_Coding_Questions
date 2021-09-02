# 96. Unique Binary Search Trees
# https://leetcode.com/problems/unique-binary-search-trees/
'''
Input: n = 3
Output: 5
Example 2:

Input: n = 1
'''
class Solution:
    def numTrees(self, n: int) -> int:
        if n<2:
            return n
        l=[0]*(n+1)
        l[0]=1
        l[1]=1
        for i in range(2,n+1):
            for j in range(0,i):
                l[i]+=l[j]*l[i-j-1]
        return l[n]