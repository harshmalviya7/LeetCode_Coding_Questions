# 1207. Unique Number of Occurrences
# https://leetcode.com/problems/unique-number-of-occurrences/
'''
Example 1:

Input: arr = [1,2,2,1,1,3]
Output: true
Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.
Example 2:

Input: arr = [1,2]
Output: false
Example 3:

Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
Output: true
'''
from collections import Counter
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        d = Counter(arr)
        s = set()
        for i in d:
            if d[i] in s:
                return False
            else:
                s.add(d[i])
        return True
