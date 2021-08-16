# 39. Combination Sum
# https://leetcode.com/problems/combination-sum/
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        a = []

        def helper(i, candidates, target, n, curr):

            if i == n:
                if 0 == target:
                    a.append(curr.copy())
                return
            if candidates[i] <= target:
                curr.append(candidates[i])

                helper(i, candidates, target - candidates[i], n, curr)
                curr.pop()

            helper(i + 1, candidates, target, n, curr)

        helper(0, candidates, target, len(candidates), [])

        return a

