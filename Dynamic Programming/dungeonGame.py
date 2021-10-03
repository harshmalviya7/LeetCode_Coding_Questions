# 174. Dungeon Game
# https://leetcode.com/problems/dungeon-game/
'''
Example 1:


Input: dungeon = [[-2,-3,3],[-5,-10,1],[10,30,-5]]
Output: 7
Explanation: The initial health of the knight must be at least 7 if he follows the optimal path: RIGHT-> RIGHT -> DOWN -> DOWN.
'''
class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:

        dp = [[0 for i in range(len(dungeon[0]))] for j in range(len(dungeon))]

        for i in range(len(dungeon) - 1, -1, -1):
            for j in range(len(dungeon[0]) - 1, -1, -1):
                if i == len(dungeon) - 1 and j == len(dungeon[0]) - 1:
                    dp[i][j] = min(0, dungeon[i][j])

                elif i == len(dungeon) - 1:
                    dp[i][j] = min(0, dp[i][j + 1] + dungeon[i][j])
                elif j == len(dungeon[0]) - 1:
                    dp[i][j] = min(0, dp[i + 1][j] + dungeon[i][j])
                else:
                    dp[i][j] = min(0, dungeon[i][j] + max(dp[i + 1][j], dp[i][j + 1]))
        return abs(dp[0][0]) + 1
