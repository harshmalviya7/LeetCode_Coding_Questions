# 735. Asteroid Collision
# https://leetcode.com/problems/asteroid-collision/

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:

        stack = []
        l = []
        i = 0
        while (i < len(asteroids)):
            while (stack and asteroids[i] < 0 < stack[-1]):
                if stack[-1] < -asteroids[i]:
                    stack.pop()
                    print("sa", stack)
                    continue
                elif stack[-1] == -asteroids[i]:
                    stack.pop()

                break
            else:
                stack.append(asteroids[i])
                print(stack)

            i += 1
        print(stack)
        return stack


