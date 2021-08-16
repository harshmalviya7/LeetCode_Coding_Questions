# 40. Combination Sum II
# https://leetcode.com/problems/combination-sum-ii/
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        def helper(i, curr, target):
            if target == 0:
                l.append(list(curr))
                return
            for j in range(i, len(candidates)):
                if j > i and candidates[j] == candidates[j - 1]:
                    continue
                if candidates[j] > target:
                    break
                curr.append(candidates[j])
                helper(j + 1, curr, target - candidates[j])
                curr.pop()

        candidates.sort()
        l = []
        helper(0, [], target)
        return l

        # def helper(i,target,curr,l):
        #     if target==0:
        #         l.append(list(curr))
        #         return
        #     if target<0:
        #         return
        #     for j in range(i,len(candidates)):
        #         if j==i or candidates[j]!=candidates[j-1]:
        #             curr.append(candidates[j])
        #             helper(j+1,target-candidates[j],curr,l)
        #             curr.pop()
        # candidates.sort()
        # l=[]
        # helper(0,target,[],l)
        # print(l)
        # return l
