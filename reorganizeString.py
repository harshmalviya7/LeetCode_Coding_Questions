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
            current = heapq.heappop(heap)[1]
            nextt = heapq.heappop(heap)[1]
            result += current
            result += nextt
            a[current] -= 1
            a[nextt] -= 1
            if a[current] > 0:
                heapq.heappush(heap, [-a[current], current])
            if a[nextt] > 0:
                heapq.heappush(heap, [-a[nextt], nextt])
            print(result)
        print(heap)
        if heap:
            last = heapq.heappop(heap)[1]
            if a[last] > 1:
                return ""
            result += last
        return (result)



