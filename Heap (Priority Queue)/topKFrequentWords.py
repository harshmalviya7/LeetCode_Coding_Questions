# 692. Top K Frequent Words
# https://leetcode.com/problems/top-k-frequent-words/
import heapq
from collections import defaultdict
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        d=defaultdict(int)
        l=[]
        for i in words:
            d[i]+=1
        for i in d:
            heapq.heappush(l,(-d[i],i))
        nums=[]
        while(k):
            nums.append(heapq.heappop(l)[1])
            k-=1
        return (nums)