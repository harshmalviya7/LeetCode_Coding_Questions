# 1313. Decompress Run-Length Encoded List
# https://leetcode.com/problems/decompress-run-length-encoded-list/
class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        l = []
        for i in range(0, len(nums) - 1, 2):
            a = [nums[i + 1]] * nums[i]
            l += a
        print(l)
        return l
