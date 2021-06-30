#767 Reorganize String
# https://leetcode.com/problems/reorganize-string/

from collections import Counter
import heapq
class Solution:
    def reorganizeString(self, s: str) -> str:
        heap = []
        a = Counter(s)
        for i, j in a.items():
            heap.append([-j, i])
        result = ""
        heapq.heapify(heap)
        print(heap)
        while (len(heap) > 1):
            current = heapq.heappop(heap)
            nextt = heapq.heappop(heap)
            result += current[1]
            result += nextt[1]
            current[0] += 1
            nextt[0] += 1
            if current[0] < 0:
                heapq.heappush(heap, current)
            if nextt[0] < 0:
                heapq.heappush(heap, nextt)
            print(result)
        print(heap)
        if heap:
            last = heapq.heappop(heap)
            if last[0] < -1:
                return ""
            result += last[1]
        return (result)

