# 239. Sliding Window Maximum
# https://leetcode.com/problems/sliding-window-maximum/

from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:


        i, j = 0, 0
        q = deque()
        n = len(nums)
        res = []
        while (j < n):
            while q and nums[j] > q[-1]:
                q.pop()
            q.append(nums[j])
            if j - i + 1 < k:
                j += 1
            elif j - i + 1 == k:
                res.append(q[0])
                if q[0] == nums[i]:
                    q.popleft()
                i += 1
                j += 1

        return res