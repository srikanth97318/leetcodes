class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = [ ]
        for ash in asteroids:
            while stack and ash < 0 and stack[-1] > 0:
                if stack[-1] < -ash:
                    stack.pop()
                    continue
                elif stack[-1] == -ash:
                    stack.pop()
                break
            else:
                stack.append(ash)
        return stack
        